from api.telegram import sendMessage
from database.queries.vip_users import selectVipUser


class Links:
    def __init__(self):
        pass

    def run(self, **kwargs):
        user = kwargs["user"]

        vip_user = selectVipUser(user["ID"])

        if vip_user and vip_user["STATUS"] == "active":
            sendMessage(user["TELEGRAM_ID"], "Ver quais links disponibilizar")
        else:
            text = "Nenhum link VIP disponível para o seu usuário \n"
            text += "Caso queira ser VIP, digite o comando /pagamento para mais informações \n"
            text += "Se acredita que isto seja um erro, entre em contato com o suporte no botão abaixo."
            buttons = [
                [
                    {
                        "text": "📱 Falar com o suporte",
                        "url": "https://financialmove.com.br/andreimeajuda",
                    }
                ]
            ]
            sendMessage(user["TELEGRAM_ID"], text, buttons)
