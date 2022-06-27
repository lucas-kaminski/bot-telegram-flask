from api.telegram import sendMessage


class Cadastro:
    def __init__(self):
        pass

    def run(self, **kwargs):
        user = kwargs["user"]

        print(user)

        text = "Informações cadastrais\n\n"
        text += f'Nome: {user["NAME"]}\n'
        text += f'Email: {user["EMAIL"]}\n'
        text += f'Telefone: {user["PHONE"]}\n'

        buttons = [
            [{"text": "✍ Atualizar nome", "callback_data": "/cadastro/updateNome"}],
            [{"text": "📩 Atualizar e-mail", "callback_data": "/cadastro/updateEmail"}],
            [
                {
                    "text": "📞 Atualizar telefone",
                    "callback_data": "/cadastro/updatePhone",
                }
            ],
        ]

        sendMessage(user["TELEGRAM_ID"], text, buttons)
