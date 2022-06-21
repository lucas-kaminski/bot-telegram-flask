from flask import Flask, request, Response, jsonify
from flask_restx import Api, Resource
import json
import stripe
import logging

from dateutil.relativedelta import relativedelta
from datetime import date

from server.instance import server

from database.queries.products import selectAllProducts, updateProduct, selectProduct
from database.queries.users import updateUser, selectUser
from database.queries.vip_users import selectVipUser, insertVipUser, updateVipUser

app, api = server.app, server.api

# TODO: Env
stripe.api_key = "sk_test_51LAXyuKaSskwmwx9kzacuFWAsMZoxam4uZi7dqDpoBXpi1CRzDoZ3QDM6DdqhOfVKBAStJVrY8gpqPiI7F7b12UA00nPdF8aqB"

endpoint_secret = 'whsec_VZWdv3AyRH3M2LQMvr94vyYl7HriOGaj'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='./src/logs/stripe.log')

@api.route('/stripe/sync/products')
class SyncStripeProducts(Resource):
  def post(self):
    products_from_database = selectAllProducts()
    products_from_stripe = stripe.Product.list()

    new_products = []
    registered_products = []

    for product in products_from_database:
      if product['STRIPE_ID'] is None:
        new_products.append(product)
      else:
        registered_products.append(product)

    # TODO: produtos desativados

    for new_product in new_products:
      stripe_product = stripe.Product.create(
        name=new_product['NAME'],
        active=True,
        description=new_product['DESCRIPTION'] if new_product['DESCRIPTION'] != '' else None,
        metadata={
          'id':new_product['ID'],
        },
        default_price_data={
          'currency': 'BRL',
          'unit_amount_decimal': str(new_product['PRICE']).replace('.',''),
          'recurring': {
            'interval': 'month',
            'interval_count': new_product['VALIDITY_IN_MONTHS'],
          }
        }
      )

    return jsonify({'status': 'ok'})

@api.route('/stripe/webhook')
class StripeWebhook(Resource):
  def post(self):
    payload = request.get_data()
    sig_header = request.headers.get('Stripe-Signature')

    try:
      event = stripe.Webhook.construct_event(
        payload=payload,
        sig_header=sig_header,
        secret=endpoint_secret,
      )
    except ValueError as e:
      return Response(status=400)
    except stripe.error.SignatureVerificationError as e:
      return Response(status=400)

    event_type = event['type']

    if event_type == 'customer.created':
      print('Customer created')
      customer = event['data']['object']
      customer_database_id = customer['metadata']['id']
      updateUser(id=customer_database_id, stripe_id=customer['id'])
    elif event_type == 'customer.deleted':
      print('Customer deleted')
      customer = event['data']['object']
      customer_database_id = customer['metadata']['id']
      updateUser(id=customer_database_id, stripe_id=None)
    elif event_type == 'product.created':
      print('Product created')
      product = event['data']['object']
      product_database_id = product['metadata']['id']
      updateProduct(id=product_database_id, stripe_id=product['id'])
    elif event_type == 'checkout.session.completed' or event_type == 'checkout.session.async_payment_succeeded':
      session = event['data']['object']
      user = selectUser(stripe_id=session['customer'])
      vip_user = selectVipUser(user_id=user['ID'])
      subscription = stripe.Subscription.retrieve(session['subscription'])
      product = selectProduct(stripe_id=subscription['plan']['product'])

      expiration_date = date.today() + relativedelta(months=+product["VALIDITY_IN_MONTHS"])

      status = 'active' if session['payment_status'] == 'paid' else 'awaiting_payment'
      print(status)
      if vip_user is None:
        print('Inserting vip user')
        insertVipUser(user_id=user['ID'], product_id=product['ID'], expiration=expiration_date, status=status)
      else:
        print('Updating vip user')
        updateVipUser(id=vip_user['ID'], expiration=expiration_date, status=status)
    elif event_type == 'invoice.paid':
      print('Invoice paid')
      invoice = event['data']['object']
      print(invoice['customer'])
      user = selectUser(stripe_id=invoice['customer'])
      vip_user = selectVipUser(user_id=user['ID'])
      subscription = stripe.Subscription.retrieve(invoice['subscription'])
      product = selectProduct(stripe_id=subscription['plan']['product'])
      expiration_date = vip_user['EXPIRATION'] + relativedelta(months=+product["VALIDITY_IN_MONTHS"])
      updateVipUser(id=vip_user['ID'], expiration=expiration_date, status='active')
    elif event_type == 'customer.subscription.deleted':
      subscription = event['data']['object']
      user = selectUser(stripe_id=subscription['customer'])
      updateVipUser(id=user['ID'], status='canceled')
    else:
      logging.info('Unknown event type: ' + event_type)

    return jsonify(received=True)
