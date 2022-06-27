from database.connection import Connection


def selectAllChannels():
    connection = Connection()
    cursor = connection.cursor

    cursor.execute(f"SELECT * FROM channels")
    channels = cursor.fetchall()

    connection.close()
    return channels


def selectChannel(id=None, telegram_id=None):
    connection = Connection()
    cursor = connection.cursor

    if telegram_id is not None:
        sql = f'SELECT * FROM channels WHERE TELEGRAM_ID = "{telegram_id}"'
        cursor.execute(sql)
    else:
        cursor.execute(f"SELECT * FROM channels WHERE ID = {id}")

    channel = cursor.fetchone()
    connection.close()

    return channel


def insertChannel(telegram_id, name):
    connection = Connection()
    cursor = connection.cursor
    cursor.execute(
        f"INSERT INTO channels (TELEGRAM_ID, NAME) VALUES ('{telegram_id}', '{name}')"
    )
    connection.commit()
    connection.close()
    return selectChannel(telegram_id=telegram_id)


def updateChannel(id=None, telegram_id=None):
    new_id = telegram_id if telegram_id is not None else "null"
    sql = f"UPDATE channels SET TELEGRAM_ID = {new_id} WHERE ID = {id}"

    connection = Connection()
    cursor = connection.cursor
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return selectChannel(id=id)
