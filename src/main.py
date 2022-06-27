from flask import request

from server.instance import server
from utils.functions import setAvaliableCommandsJson
from controllers.telegram import Telegram, setCommands, setWebhook
from controllers.stripe import SyncStripeProducts, StripeWebhook, SetWebhook
from controllers.internal import NewCoin, Ping
from controllers.evermart import EvermartWebhook

import logging
from logging.handlers import RotatingFileHandler

from time import strftime

app = server.app

# https://gist.github.com/alexaleluia12/e40f1dfa4ce598c2e958611f67d28966
@app.after_request
def after_request(response):
    timestamp = strftime("[%Y-%b-%d %H:%M:%S]")
    logger = logging.getLogger("tdm")
    print(
        f"{timestamp} {request.remote_addr} {request.method} {request.scheme} {request.full_path} {response.status}"
    )
    logger.error(
        f"{timestamp} {request.remote_addr} {request.method} {request.scheme} {request.full_path} {response.status}"
    )
    return response


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
