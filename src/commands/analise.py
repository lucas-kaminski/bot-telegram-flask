from api.telegram import sendMessage

from database.queries.analises import selectLastAnalise
from datetime import datetime

class Analise():
  def __init__ (self):
    pass

  def run(self, **kwargs):
    user = kwargs['user']
    analise = selectLastAnalise()

    print(analise)

    text = f'<b>{analise["TITLE"]} 📊📈📉\n\n</b>'
    text += f'<b>📅 Postada em: </b> {analise["UPDATED_AT"].strftime("%d/%m/%Y %H:%M:%S")}\n\n'
    text += f'💲 <b>Preço agora (BINANCE - USDT)</b>: $ pegar da api \n\n'
    text += f'{analise["BODY"]}'
    text += f'\n\n'
    text += f'Por: pegar username do autor\n'
    text += f'{analise["LINK"]}'


    sendMessage(user['TELEGRAM_ID'], text, parse_mode='HTML')
