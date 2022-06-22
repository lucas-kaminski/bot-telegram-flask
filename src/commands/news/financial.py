from api.telegram import updateMessage


class Financial():
    def __init__(self):
        pass

    def run(self, **kwargs):
        user = kwargs['user']
        message_id = kwargs['message_id']
        print(user)

        text = "Clique no botão abaixo para ler as notícias e artigos mais recentes no site da Financial Move."
        buttons = [
            [
                {
                    'text': "Abrir site",
                    'url': "https://www.financialmove.com.br"
                }]
        ]

        text = 'Escolha a fonte das notícias:'

        updateMessage(user['TELEGRAM_ID'], message_id, text, buttons)
