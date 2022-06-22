from server.instance import server

from controllers.telegram import Telegram
from controllers.stripe import SyncStripeProducts, StripeWebhook, SetWebhook

server.run()
