from flask import request

from server.instance import server
from controllers.telegram import Telegram, setCommands, setWebhook
from controllers.stripe import SyncStripeProducts, StripeWebhook, SetWebhook
from controllers.internal import NewCoin
from controllers.evermart import EvermartWebhook

import logging
from logging.handlers import RotatingFileHandler

import json

from time import strftime

app = server.app

# https://gist.github.com/alexaleluia12/e40f1dfa4ce598c2e958611f67d28966
@app.after_request
def after_request(response):
    timestamp = strftime("[%Y-%b-%d %H:%M:%S]")
    print(
        f"{timestamp} {request.remote_addr} {request.method} {request.scheme} {request.full_path} {response.status}"
    )
    logger.error(
        f"{timestamp} {request.remote_addr} {request.method} {request.scheme} {request.full_path} {response.status}"
    )
    return response


def setAvaliableCommandsJson():
    with open("src/json/commands.json", encoding="utf8") as json_file:
        commands = json.load(json_file)["commands"]

    available_commands = {"available_commands": []}
    for command in commands:
        available_commands["available_commands"].append(command["command"])

    with open("src/json/availableCommands.json", "w", encoding="utf8") as json_file:
        json.dump(available_commands, json_file)


if __name__ == "__main__":
    # Logging
    handler = RotatingFileHandler("./src/logs/app.log", maxBytes=100000, backupCount=3)
    logger = logging.getLogger("tdm")
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)

    # Settings
    setAvaliableCommandsJson()

    # Server
    server.run()
