from api.telegram import sendMessage

import json


class Help:
    def __init__(self):
        pass

    def run(self, **kwargs):
        user = kwargs["user"]
        with open("src/json/commands.json", encoding="utf8") as json_file:
            commands = json.load(json_file)["commands"]

        text = "*Comandos disponíveis no bot*\n\n"
        for command in commands:
            text += "*/" + command["command"] + "* - " + command["description"] + "\n"

        sendMessage(user["TELEGRAM_ID"], text)
