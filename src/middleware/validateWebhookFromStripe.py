from flask import request, Response

import stripe

# TODO: Env
stripe.api_key = "sk_test_51LAXyuKaSskwmwx9kzacuFWAsMZoxam4uZi7dqDpoBXpi1CRzDoZ3QDM6DdqhOfVKBAStJVrY8gpqPiI7F7b12UA00nPdF8aqB"

endpoint_secret = 'whsec_hCurOXHwhQqmyLXN7QLfFriUOumjPGBK'

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
