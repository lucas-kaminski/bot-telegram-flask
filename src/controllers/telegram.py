from flask import Flask, request, Response
from flask_restx import Api, Resource
import json

from server.instance import server
from api.telegram import sendMessage, setWebhook, setCommands
from middleware.identificateMessageFromTelegram import identificateMessageFromTelegram


app, api = server.app, server.api

with open("/src/json/availableCommands.json", encoding="utf8") as json_file:
    valid_commands = json.load(json_file)["available_commands"]

@api.route("/telegram/set/webhook")
class SetWebhook(Resource):
    def post(self):
        url = request.get_json()["url"]
        setWebhook(url + "/telegram/webhook")
        return True


@api.route("/telegram/set/commands")
class SetCommands(Resource):
    def put(self):
        setCommands()
        return True


app.before_request(identificateMessageFromTelegram)


@api.route("/telegram/webhook")
class Telegram(Resource):
    def post(self):
        # Definido no message validation
        args = request.args
        message_type = args["message_type"]
        if message_type == "message":
            message_sent_formatted = (
                args["message_sent"].split(" ")[0].removeprefix("/")
            )
            message_sent_data = args["message_sent"].split(" ")[1:]

            if message_sent_formatted in valid_commands:
                package = f"commands.{message_sent_formatted}"
                name = message_sent_formatted[:1].upper() + message_sent_formatted[1:]
                command = getattr(__import__(package, fromlist=[name]), name)
                command.run(
                    self, user=args["user"], message_sent_data=message_sent_data
                )
            else:
                text = "Comando inválido."
                sendMessage(args["user"]["TELEGRAM_ID"], text)

        elif message_type == "callback":

            callback_path = args["callback_path"]
            package = f"commands{callback_path}"
            class_name = callback_path.split(".")[-1]
            name = class_name[:1].upper() + class_name[1:]  # Capitalize first letter
            callback = getattr(__import__(package, fromlist=[name]), name)
            callback.run(
                self,
                user=args["user"],
                message_id=args["message_id"],
                callback_info=args["callback_info"],
            )

        elif message_type == "channel_post":
            channel = args["channel"]
            print(channel)

        else:
            print("outro")
