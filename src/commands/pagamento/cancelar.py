from api.telegram import deleteMessage

class Cancelar():
  def __init__ (self):
    pass

  def run(self, **kwargs):
    user = kwargs['user']
    message_id = kwargs['message_id']

    deleteMessage(chat_id=user['TELEGRAM_ID'], message_id=message_id)
