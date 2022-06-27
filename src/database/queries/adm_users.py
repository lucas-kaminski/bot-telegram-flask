from database.connection import Connection


def selectAdmUser(id=None):
    connection = Connection()
    cursor = connection.cursor

    if id is not None:
        cursor.execute(f"SELECT * FROM adm_users WHERE ID = {id}")
        adm_user = cursor.fetchone()
    else:
        adm_user = None

    connection.close()
    return adm_user

def updateAdmUser(id, archive):
    connection = Connection()
    cursor = connection.cursor

    cursor.execute(f"UPDATE adm_users SET ARCHIVE = '{archive}' WHERE ID = {id}")

    connection.commit()
    connection.close()
    return True
