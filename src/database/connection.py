import mysql.connector
from dotenv import load_dotenv
load_dotenv()
import os

config = {
    "user": os.environ.get("MYSQL_USER"),
    "password": os.environ.get("MYSQL_PASSWORD"),
    "database": os.environ.get("MYSQL_DATABASE"),
    "host": os.environ.get("MYSQL_HOST"),
    "raise_on_warnings": True,
}


class Connection:
    def __init__(self):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor(buffered=True, dictionary=True)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
