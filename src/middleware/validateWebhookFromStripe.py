from flask import request, Response

from dotenv import load_dotenv
load_dotenv()
import os

import stripe

endpoint_secret = os.environ.get('STRIPE_WEBHOOK_SECRET')

def validateWebhookFromStripe():
  if request.endpoint == 'stripe_webhook':
    payload = request.get_data()
    sig_header = request.headers.get('Stripe-Signature')

    try:
      event = stripe.Webhook.construct_event(
        payload=payload,
        sig_header=sig_header,
        secret=endpoint_secret,
      )
      request.args = {'event': event}
    except ValueError as e:
      return Response(status=400)
    except stripe.error.SignatureVerificationError as e:
      return Response(status=400)
