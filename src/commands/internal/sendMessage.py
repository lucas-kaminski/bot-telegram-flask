from api.telegram import sendMessage, updateMessage
from database.queries.users import selectAllUsers
from database.queries.adm_users import selectAdmUser
from database.queries.channels import selectAllChannels


class SendMessage:
    def __init__(self):
        pass

    def run(self, **kwargs):
        user = kwargs["user"]
        adm_user = selectAdmUser(id=user["ID"])
        message_id = kwargs["message_id"]
        callback_info = kwargs["callback_info"]
        print(callback_info)

        user = callback_info.split("&")
        user = user[0].split("=")[1]

        channel = callback_info.split("&")
        channel = channel[1].split("=")[1]

        updateMessage(
            user["TELEGRAM_ID"],
            message_id,
            text="Está sendo feito o processo de envio de mensagem...",
        )

        if user:
            for user in selectAllUsers():
                print(user)
                sendMessage(
                    chat_id=user["TELEGRAM_ID"], text=adm_user["ARCHIVE"].decode()
                )

        if channel:
            for channel in selectAllChannels():
                print(channel)
                try:
                    sendMessage(
                        chat_id=channel["TELEGRAM_ID"],
                        text=adm_user["ARCHIVE"].decode(),
                    )
                except Exception as e:
                    print(e)
                    print("Error: unable to send message")

        updateMessage(
            user["TELEGRAM_ID"], message_id, text="Mensagens enviadas com sucesso!"
        )
