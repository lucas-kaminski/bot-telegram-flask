from api.telegram import updateMessage
from database.queries.products import selectAllProducts

class CartaoOuBoleto():
  def __init__ (self):
    pass

  def run(self, **kwargs):
    products = selectAllProducts()
    buttons = []
    user = kwargs['user']
    message_id = kwargs['message_id']

    for product in products:
      buttons.append([
        {
          'text': f'{product["NAME"]} - R$ {product["PRICE"]}',
          'callback_data': f'/pagamento/assinaturaSelecionada:{product["ID"]}'
        }
      ])

    updateMessage(user['TELEGRAM_ID'], message_id, 'Selecione uma das opções de assinatura abaixo:', buttons)
