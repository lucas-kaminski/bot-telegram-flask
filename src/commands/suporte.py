from api.telegram import sendMessage


class Suporte:
    def __init__(self):
        pass

    def run(self, **kwargs):
        user = kwargs["user"]

        text = "Clique no botão abaixo para falar com o suporte.\n"
        text += "Você será direcionado para o whatsapp do Financial Move."

        buttons = [
            [
                {
                    "text": "📱 Falar com o suporte",
                    "url": "https://financialmove.com.br/andreimeajuda",
                }
            ]
        ]

        sendMessage(user["TELEGRAM_ID"], text, buttons)
