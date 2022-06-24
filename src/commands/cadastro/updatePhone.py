from api.telegram import updateMessage
from database.queries.users import updateUser


class UpdatePhone:
    def __init__(self):
        pass

    def run(self, **kwargs):
        user = kwargs["user"]
        message_id = kwargs["message_id"]
        callback_info = kwargs["callback_info"]
        status = "awaiting_phone" if callback_info == "first_time" else "updating_phone"
        updateUser(id=user["ID"], status=status)

        updateMessage(user["TELEGRAM_ID"], message_id, text="Envie seu telefone")
