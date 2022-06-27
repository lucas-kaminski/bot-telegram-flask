from api.telegram import sendMessage

import requests
import json


class Listarmoedas:
    def __init__(self):
        pass

    def run(self, **kwargs):
        url = "https://api-testnet.bybit.com/v2/public/tickers"
        data = requests.get(url).json()["result"]
        user = kwargs["user"]

        # sort from highest to price
        data = sorted(data, key=lambda x: float(x["last_price"]), reverse=True)[:5]

        # get coins from jso
        json_coins = {"coins": [{}]}

        with open("src/json/coins.json") as json_file:
            json_coins = json.load(json_file)

        coins_in_json = [coin["symbol"] for coin in json_coins["coins"]]

        for coin in data:
            if coin["symbol"] in coins_in_json:
                json_coins["coins"][coins_in_json.index(coin["symbol"])] = {
                    "symbol": coin["symbol"],
                    "last_price": coin["last_price"],
                }
            else:
                json_coins["coins"].append(
                    {"symbol": coin["symbol"], "last_price": coin["last_price"]}
                )

        # rewrite the json
        with open("src/json/coins.json", "w") as json_file:
            json.dump(json_coins, json_file)

        bigger_name_size = max([len(x["symbol"]) for x in data])

        text = "Lista de moedas: \n"

        for x in json_coins["coins"]:
            text += "{:<{}} - {}\n".format(
                x["symbol"], bigger_name_size, x["last_price"]
            )

        sendMessage(user["TELEGRAM_ID"], text)
