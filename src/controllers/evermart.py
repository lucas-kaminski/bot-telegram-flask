from server.instance import server

from flask import Flask, request
from flask_restx import Api, Resource

app, api = server.app, server.api


@api.route("/evermart/webhook")
class EvermartWebhook(Resource):
    def post(self):
        print("evermart webhook")
