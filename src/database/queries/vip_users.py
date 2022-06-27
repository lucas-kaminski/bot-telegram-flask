from database.connection import Connection


def selectVipUser(user_id):
    connection = Connection()
    cursor = connection.cursor

    sql = f"SELECT * FROM vip_users WHERE USER_ID = {user_id}"
    cursor.execute(sql)

    vip_user = cursor.fetchone()
    connection.close()

    return vip_user


def insertVipUser(user_id, product_id, expiration, status):
    connection = Connection()
    cursor = connection.cursor

    sql = f'INSERT INTO vip_users (USER_ID, PRODUCT_ID, EXPIRATION, STATUS) VALUES ({user_id}, {product_id}, "{expiration}", "{status}")'
    cursor.execute(sql)
    connection.commit()
    connection.close()

    return selectVipUser(user_id)


def updateVipUser(id, user_id=None, product_id=None, expiration=None, status=None):
    connection = Connection()
    cursor = connection.cursor

    params = {
        "USER_ID": user_id,
        "PRODUCT_ID": product_id,
        "EXPIRATION": expiration,
        "STATUS": status,
    }

    sql = "UPDATE vip_users SET "

    for key, value in params.items():
        if value is not None:
            sql += f"{key} = '{value}', "

    sql = sql[:-2]

    sql += f" WHERE ID = {id}"

    cursor.execute(sql)
    connection.commit()
    connection.close()

    return selectVipUser(id)
