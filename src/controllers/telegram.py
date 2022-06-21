from flask import Flask, request
from flask_restx import Api, Resource

from server.instance import server
from api.telegram import sendMessage

from middleware.messageValidation import messageValidation

app, api = server.app, server.api

app.before_request(messageValidation)

@api.route('/telegram')
class Telegram(Resource):
  def post(self):
    # Definido no message validation
    args = request.args
    message_type = args['message_type']

    if (message_type == 'message'):

      # TODO: Validação via JSON do setCommands
      valid_commands = ['listarmoedas', 'news', 'pagamento', 'trades', 'analise', 'carteiradotasso', 'fear', 'help', 'links', 'settings', 'start', 'suporte', 'tutoriais']

      message_sent_formatted = args['message_sent'].split(' ')[0].removeprefix('/')
      message_sent_data = args['message_sent'].split(' ')

      if message_sent_formatted in valid_commands:
        package = f'commands.{message_sent_formatted}'
        name = message_sent_formatted[:1].upper() + message_sent_formatted[1:]
        command = getattr(__import__(package, fromlist=[name]), name)
        command.run(self, user=args['user'], message_sent_data=message_sent_data)
      else:
        text = 'Comando inválido.'
        sendMessage(user['TELEGRAM_ID'], text)

    elif (message_type == 'callback'):

        callback_path = args['callback_path']
        package = f'commands.{callback_path}'
        class_name = callback_path.split('.')[-1]
        name = class_name[:1].upper() + class_name[1:] # Capitalize first letter
        callback = getattr(__import__(package, fromlist=[name]), name)
        callback.run(self, user=args['user'], message_id=args['message_id'], callback_info=args['callback_info'])

    elif (message_type == 'channel_post'):
      print('channel_post')

    else:
      print('outro')











