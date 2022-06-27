from server.instance import server

from flask import Flask, request
from flask_restx import Api, Resource

app, api = server.app, server.api


@api.route("/evermart/webhook")
class EvermartWebhook(Resource):
    def get(self):
        return {"status": "ok"}

    def post(self):

        print("evermart webhook")
