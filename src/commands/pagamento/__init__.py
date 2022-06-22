from api.telegram import sendMessage

class Pagamento():
  def __init__ (self):
    pass

  def run(self, **kwargs):
    user = kwargs['user']
    buttons = [
    [
      {
        'text': "Continuar com cartão ou boleto",
        'callback_data': "/pagamento/cartaoOuBoleto"
      }
    ],
    [
      {
        'text': "Continuar com pix ou cripto",
        'url': "https://financialmove.com.br/CrisMeAjuda"
      },
    ],
    [
      {
        'text': "📩 Atualizar e-mail",
        'callback_data': "/cadastro/updateEmail"
      }
    ]
  ]

    text = 'Estou aqui para facilitar o pagamento referente aos serviços prestados pela Financial Move\n'
    text += 'Por aqui aceitamos pagamento por cartão de crédito, mas também trabalhamos com Pix, Criptos e Boleto...\n'
    text += 'Nós não temos e nem desejamos nenhum acesso referente ao seu cartão de crédito..ok?\n\n'
    text += f'Certifique-se de utilizar o mesmo email cadastrado no bot ({user["EMAIL"]}) para fazer os pagamentos.'

    sendMessage(user['TELEGRAM_ID'], text, buttons)
