from api.telegram import sendPhoto

import requests
import datetime as dt


class Fear:
    def __init__(self):
        pass

    def run(self, **kwargs):
        user = kwargs["user"]

        response = requests.get("https://api.alternative.me/fng/?limit=30").json()
        data = response["data"]

        seconds_to_update_splitted = str(
            dt.timedelta(seconds=int(data[0]["time_until_update"]))
        ).split(":")
        seconds_to_update_formatted = "{} horas, {} minutos e {} segundos".format(
            seconds_to_update_splitted[0],
            seconds_to_update_splitted[1],
            seconds_to_update_splitted[2],
        )

        text = f'*📊 {response["name"]} 💰*\n\n'
        text += (
            "*⚡️ Hoje:* "
            + str(data[0]["value"])
            + " - "
            + str(data[0]["value_classification"])
            + "\n\n"
        )
        text += (
            "*⚡️ Ontem:* "
            + str(data[1]["value"])
            + " - "
            + str(data[1]["value_classification"])
            + "\n\n"
        )
        text += (
            "*⚡️ Semana passada:* "
            + str(data[6]["value"])
            + " - "
            + str(data[6]["value_classification"])
            + "\n\n"
        )
        text += (
            "*⚡️ Mês passado:* "
            + str(data[29]["value"])
            + " - "
            + str(data[29]["value_classification"])
            + "\n\n"
        )
        text += "Próxima atualização em " + seconds_to_update_formatted + "\n\n"

        sendPhoto(
            chat_id=user["TELEGRAM_ID"],
            photo="https://alternative.me/crypto/fear-and-greed-index.png",
            caption=text,
        )
