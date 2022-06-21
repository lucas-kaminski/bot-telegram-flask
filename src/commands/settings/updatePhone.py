from api.telegram import updateMessage

class UpdatePhone():
  def __init__ (self):
    pass

  def run(self, **kwargs):
    user = kwargs['user']
    message_id = kwargs['message_id']

    updateMessage(user['TELEGRAM_ID'], message_id, text='Envie seu telefone')
