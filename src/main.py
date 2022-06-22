from server.instance import server

from controllers.telegram import Telegram, setCommands, setWebhook
from controllers.stripe import SyncStripeProducts, StripeWebhook, SetWebhook
from controllers.external import NewCoin

server.run()
