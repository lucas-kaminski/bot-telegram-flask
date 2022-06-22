from api.telegram import sendMessage

class Start():
  def __init__ (self):
    pass

  def run(self, **kwargs):
    user = kwargs['user']

    text = 'Você já está cadastrado em nosso sistema.\n'
    text += 'Para mais informações, clique ou digite /help.'

    sendMessage(user['TELEGRAM_ID'], text)
