from flask import Flask
from flask_restx import Api


class Server:
    def __init__(
        self,
    ):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version="1.0",
            title="WTLL Bot",
            description="Bot criado em Python para o WTLL",
            doc="/docs",
        )

    def run(
        self,
    ):
        self.app.run(debug=True, host="0.0.0.0", port=5000)


server = Server()
