from flask import Flask, request
from flask_restx import Api, Resource
import json

from server.instance import server
from database.queries.users import selectAllUsers, selectUser
from database.queries.adm_users import updateAdmUser
from database.queries.channels import selectAllChannels
from api.telegram import sendMessage
from commands.listarmoedas import Listarmoedas
from middleware.authenticateAdmin import authenticateAdmin

app, api = server.app, server.api


@api.route("/ping")
class Ping(Resource):
    def get(self):
        return "Pong"

app.before_request(authenticateAdmin)
@api.route("/admin/new/message")
class NewMessage(Resource):
    def post(self):
        message = request.get_json()['message']

        send_to_users = request.get_json()['send_to_users']
        send_to_channels = request.get_json()['send_to_channels']

        adm_user = request.args['adm_user']

        user = selectUser(id=adm_user['ID'])

        message_to_adm = 'Ao confirmar, a mensagem a seguir será enviada para: \n\n'
        if send_to_users is not None:
            message_to_adm += '*Usuários*'
            message_to_adm += '\n'
        if send_to_channels is not None:
            message_to_adm += '*Canais*'
            message_to_adm += '\n'
        message_to_adm += '\n'
        message_to_adm += message

        callback_info = 'user=true' if send_to_users is not None else 'user=false'
        callback_info += '&channel=true' if send_to_channels is not None else '&channel=false'

        buttons = [
            [
                {
                    'text':'Confirmar',
                    'callback_data':'/internal/sendMessage:' + callback_info
                }
            ],
            [
                {
                    'text':'Cancelar',
                    'callback_data':'/internal/cancelar'
                }
            ]
        ]

        updateAdmUser(id=adm_user['ID'], archive=message)

        sendMessage(chat_id=user['TELEGRAM_ID'], text=message_to_adm, buttons=buttons)

        return 'Mensagem enviada'

@api.route("/admin/new/coin")
class NewCoin(Resource):
    def post(self):
        symbol = request.get_json()["symbol"]
        last_price = request.get_json()["last_price"]

        with open("src/json/coins.json", "r") as json_file:
            json_coins = json.load(json_file)

        coins_in_json = [coin["symbol"] for coin in json_coins["coins"]]

        if symbol in coins_in_json:
            json_coins["coins"][coins_in_json.index(symbol)] = {
                "symbol": symbol,
                "last_price": last_price,
            }
        else:
            json_coins["coins"].append({"symbol": symbol, "last_price": last_price})

        with open("src/json/coins.json", "w") as json_file:
            json.dump(json_coins, json_file)

        users = selectAllUsers()
        channels = selectAllChannels()

        for user in users:
            if user["TELEGRAM_ID"] is not None:
                listarmoedas = Listarmoedas()
                sendMessage(
                    user["TELEGRAM_ID"],
                    f"Moeda {symbol} recentemente adicionada na listagem, confira como está agora!",
                )
                listarmoedas.run(user=user)

        for channel in channels:
            if channel["TELEGRAM_ID"] is not None:
                sendMessage(
                    channel["TELEGRAM_ID"],
                    f"Moeda {symbol} recentemente adicionada na listagem, confira como está agora!",
                )
                listarmoedas.run(user=channel)

        return {"status": "ok"}
