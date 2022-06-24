import mysql.connector

config = {
    "user": "b83db321a0c624",
    "password": "4c21997e",
    "host": "us-cdbr-east-05.cleardb.net",
    "database": "heroku_a84f38c7a0a02f9",
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
