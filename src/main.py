from server.instance import server
from time import strftime
from flask import request

import logging
from logging.handlers import RotatingFileHandler

from controllers.telegram import Telegram, setCommands, setWebhook
from controllers.stripe import SyncStripeProducts, StripeWebhook, SetWebhook
from controllers.internal import NewCoin

app = server.app

@app.after_request
def after_request(response):
  print('logging')
  timestamp = strftime('[%Y-%b-%d %H:%M:%S]')
  print(f'{timestamp} {request.remote_addr} {request.method} {request.scheme} {request.full_path} {response.status}')
  logger.error(f'{timestamp} {request.remote_addr} {request.method} {request.scheme} {request.full_path} {response.status}')
  return response

if __name__ == '__main__':
  # Logging
  handler = RotatingFileHandler('./src/logs/app.log', maxBytes=100000, backupCount=3)
  logger = logging.getLogger('tdm')
  logger.setLevel(logging.ERROR)
  logger.addHandler(handler)

  # Server
  server.run()
