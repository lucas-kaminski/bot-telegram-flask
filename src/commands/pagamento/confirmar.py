from api.telegram import updateMessage
from database.queries.products import selectProduct

import datetime
import stripe

class Confirmar():
  def __init__ (self):
    pass

  def run(self, **kwargs):
    user = kwargs['user']
    message_id = kwargs['message_id']
    id_product = kwargs['callback_info']

    product_database = selectProduct(id_product)

    if product_database['STRIPE_ID'] is None:
      print('Need sync products')
      return

    product_stripe = stripe.Product.retrieve(product_database['STRIPE_ID'])

    if user['STRIPE_ID'] is None:
      customer = stripe.Customer.create(
        name=user['NAME'],
        email=user['EMAIL'],
        phone=user['PHONE'],
        description='Criado ao confirmar o pagamento do produto: ' + product_database['NAME'] + 'no dia ' + str(datetime.datetime.now()),
        metadata={
          'id': user['ID'],
        })
    else:
      customer = stripe.Customer.retrieve(user['STRIPE_ID'])

    session = stripe.checkout.Session.create(
      success_url='https://www.example.com/success',
      cancel_url='https://www.example.com/cancel',
      customer=customer['id'],
      mode='subscription',
      line_items=[
        {
          'price': product_stripe['default_price'],
          'quantity': 1,
        }
      ]
    )

    text = 'Para confirmar o pagamento, acesse o link abaixo:'

    buttons = [
      [{'text': 'Efetuar o pagamento', 'url': session['url']}]
    ]

    updateMessage(chat_id=user['TELEGRAM_ID'], message_id=message_id, text=text, buttons=buttons)



