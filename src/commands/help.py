from api.telegram import sendMessage

class Help():
  def __init__ (self):
    pass

  def run(self, **kwargs):
    chat_id = kwargs['chat_id']

    sendMessage(chat_id, 'Comando a ser feito')
