from api.telegram import updateMessage
from database.queries.users import updateUser

class UpdateNome():
  def __init__ (self):
    pass

  def run(self, **kwargs):
    user = kwargs['user']
    message_id = kwargs['message_id']
    callback_info = kwargs['callback_info']

    updateUser(id=user['ID'], status='updating_name')

    updateMessage(user['TELEGRAM_ID'], message_id, text='Envie seu nome')
