from database.connection import Connection


def selectAllProducts():
    connection = Connection()
    cursor = connection.cursor

    cursor.execute(f"SELECT * FROM products")
    products = cursor.fetchall()

    connection.close()
    return products


def selectProduct(id=None, stripe_id=None):
    connection = Connection()
    cursor = connection.cursor

    if stripe_id is not None:
        sql = f'SELECT * FROM products WHERE STRIPE_ID = "{stripe_id}"'
        cursor.execute(sql)
    else:
        cursor.execute(f"SELECT * FROM products WHERE ID = {id}")

    product = cursor.fetchone()

    connection.close()
    return product


def updateProduct(id, stripe_id):
    connection = Connection()
    cursor = connection.cursor

    cursor.execute(f'UPDATE products SET STRIPE_ID = "{stripe_id}" WHERE ID = {id}')
    product = cursor.fetchone()

    connection.commit()
    connection.close()
    return product
