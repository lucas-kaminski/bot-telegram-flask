from api.telegram import sendMessage

class News():
  def __init__ (self):
    pass

  def run(self, **kwargs):
    user = kwargs['user']
    print(user)

    buttons = [
      [{
        'text': "Financial Move",
        'callback_data': "/news/financial",
      },
      {
        'text': "Outros sites",
        'callback_data': "/news/others",
      }]
    ]

    text = 'Escolha a fonte das notícias:'

    sendMessage(user['TELEGRAM_ID'], text, buttons)
