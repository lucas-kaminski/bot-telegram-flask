from flask import Flask, request
from flask_restx import Api, Resource
import json

from server.instance import server
from database.queries.users import selectAllUsers
from database.queries.channels import selectAllChannels
from api.telegram import sendMessage
from commands.listarmoedas import Listarmoedas

app, api = server.app, server.api

@api.route('/internal/newcoin')
class NewCoin (Resource):
  def post(self):
    symbol = request.get_json()['symbol']
    last_price = request.get_json()['last_price']

    with open('src/json/coins.json', 'r') as json_file:
      json_coins = json.load(json_file)

    coins_in_json = [coin['symbol'] for coin in json_coins['coins']]

    if symbol in coins_in_json:
      json_coins['coins'][coins_in_json.index(symbol)] = {'symbol': symbol, 'last_price': last_price}
    else:
      json_coins['coins'].append({'symbol': symbol, 'last_price': last_price})

    with open('src/json/coins.json', 'w') as json_file:
      json.dump(json_coins, json_file)

    users = selectAllUsers()
    channels = selectAllChannels()

    for user in users:
      if user['TELEGRAM_ID'] is not None:
        listarmoedas = Listarmoedas()
        sendMessage(user['TELEGRAM_ID'], f'Moeda {symbol} recentemente adicionada na listagem, confira como está agora!')
        listarmoedas.run(user=user)


    for channel in channels:
      if channel['TELEGRAM_ID'] is not None:
        sendMessage(channel['TELEGRAM_ID'], f'Moeda {symbol} recentemente adicionada na listagem, confira como está agora!')
        listarmoedas.run(user=channel)

    return {'status': 'ok'}

