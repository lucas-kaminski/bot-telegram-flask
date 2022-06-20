from flask import Flask
from flask_restx import Api, Resource

from server.instance import server
from utils.validation import isValidEmail, isValidPhone
from api.telegram import sendMessage

from database.queries.users import selectUser, insertUser, updateUser

app, api = server.app, server.api

@api.route('/telegram')
class Telegram(Resource):
  def get(self):
    return {'status': 'Hello World!'}

  # TODO: Colocar o middleware de validation
  def post(self):
    body = api.payload

    body_keys = body.keys()

    if ('message' in body_keys):
      chat_id = body['message']['chat']['id']
      message_sent = body['message']['text']
      from_id = body['message']['from']['id']
      from_name = body['message']['from']['first_name']
      from_name2 = body['message']['from']['last_name']

      print('Recebendo mensagem direta do telegram: ', message_sent)

      # Variável orquestradora de ações, possíveis definições:
      # - send_email_message: Envia a mensagem pedindo o email do usuário
      # - validate_email: Valida se o email é permitido e se sim
      # - send_phone_message: Envia a mensagem pedindo o telefone do usuário
      # - validate_phone: Valida se o telefone é permitido e se sim,
      # - validation_completed: O usuário acabou de finalizar o cadastro, irá alterar a mensagem para '/tutorial' para que o usuário possa receber o tutorial
      # - validated: Usuário validado, irá entrar no bloco de comandos direto
      transaction_state = ''

      # Verifica se o usuário já está cadastrado, se sim, define a transação, se não, cadastra e encerra ela
      user = selectUser(telegram_id=from_id)
      if user is not None:
        # Define o estado da transação baseado no status do usuário
        # - awaiting_email, updating_email, awaiting_phone, updating_phone, completed
        if user['STATUS'] == 'awaiting_email' or user['STATUS'] == 'updating_email':
          transaction_state = 'validate_email'
        elif user['STATUS'] == 'awaiting_phone' or user['STATUS'] == 'updating_phone':
          transaction_state = 'validate_phone'
        elif user['STATUS'] == 'completed':
          transaction_state = 'validated'
      else:
        user = insertUser(chat_id=chat_id, name=from_name, status='awaiting_email')
        text = f'Olá, {user["NAME"]}! \n \n'
        text += 'Seja muito bem vindo ao nosso bot! \n \n'
        text += 'Identificamos que você não possui um cadastro no nosso sistema.'
        sendMessage(chat_id, text)
        transaction_state = 'send_email_message'

      if (transaction_state == 'validate_email'):
        if (isValidEmail(message_sent)):
          user = updateUser(id=user['ID'], email=message_sent, status='awaiting_phone')
          transaction_state = 'send_phone_message'
        else:
          text = 'Por favor, informe um email válido.'
          sendMessage(chat_id, text)

      if user['EMAIL'] is None or transaction_state == 'send_email_message':
        text = 'Para continuar, informe seu e-mail:'
        buttons = [[{ "text": '📩 Cadastrar email', "callback_data": 'settings/updateEmail' }]]
        sendMessage(chat_id, text, buttons)
        return

      if (transaction_state == 'validate_phone'):
        if (isValidPhone(message_sent)):
          user = updateUser(id=user['ID'], phone=message_sent, status='completed')
          transaction_state = 'validation_completed'
        else:
          text = 'Por favor, informe um telefone válido.'
          sendMessage(chat_id, text)

      if user['PHONE'] is None or transaction_state == 'send_phone_message':
        text = 'Para continuar, informe seu telefone:'
        buttons = [[{ "text": '📞 Cadastrar telefone', "callback_data": 'settings/updatePhone' }]]
        sendMessage(chat_id, text, buttons)
        return

      if (transaction_state == 'validation_completed'):
        text = 'O seu cadastro foi concluído! \n\n'
        text += 'Muito bem vindo ao bot da Financial Move \n\n'
        text += 'Para começarmos, enviaremos algumas informações sobre o que você pode fazer com o bot.'
        sendMessage(chat_id, text)
        message_sent = '/tutoriais'
        transaction_state = 'validated'

      # Validado, ira importar o comando e executa-lo
      # TODO: Validação via JSON do setCommands
      valid_commands = ['listarmoedas', 'news', 'pagamento', 'trades', 'analise', 'carteiradotasso', 'fear', 'help', 'links', 'settings', 'start', 'suporte', 'tutoriais']
      if transaction_state == 'validated':
        message_sent_formatted = message_sent.split(' ')[0].removeprefix('/')
        if message_sent_formatted in valid_commands:
          package = f'commands.{message_sent_formatted}'
          name = message_sent_formatted[:1].upper() + message_sent_formatted[1:]
          command = getattr(__import__(package, fromlist=[name]), name)
          command.run(self, chat_id=chat_id, message_sent=message_sent)
        else:
          text = 'Comando inválido.'
          sendMessage(chat_id, text)
      else:
        text = 'Erro ao validar o usuário.'
        sendMessage(chat_id, text)
    elif ('callback_query' in body):
      chat_id = body['callback_query']['message']['chat']['id']
      callback_data = body['callback_query']['data']
      message_id = body['callback_query']['message']['message_id']
      user = selectUser(telegram_id=chat_id)
      if user is not None:
        print('Recebendo callback do telegram: ', callback_data)
        callback_path = callback_data.split(':')[0].replace('/', '.')
        if len(callback_data.split(':')) > 1:
          callback_info = callback_data.split(':')[1]
        else:
          callback_info = None
        package = f'commands.{callback_path}'
        name_ = callback_path.split('.')[-1]
        name = name_[:1].upper() + name_[1:]
        callback = getattr(__import__(package, fromlist=[name]), name)
        callback.run(self, chat_id=chat_id, message_id=message_id, callback_info=callback_info)
      else:
        print('Usuário não encontrado')

    elif ('channel_post' in body):
      print('channel_post')
    else:
      print('outro')











