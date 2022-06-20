from connection import Connection

def dropAllTables():
    connection = Connection()
    cursor = connection.cursor

    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    try:
      cursor.execute("DROP TABLE IF EXISTS users")
    except:
      print("Error: unable to drop table users")

    try:
      cursor.execute("DROP TABLE IF EXISTS channels")
    except:
      print("Error: unable to drop table channels")

    try:
      cursor.execute("DROP TABLE IF EXISTS products")
    except:
      print("Error: unable to drop table products")

    try:
      cursor.execute("DROP TABLE IF EXISTS vip_users")
    except:
      print("Error: unable to drop table vip_users")

    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    print("Tables dropped")
    connection.commit()
    connection.close()

def createUsersTable():
    connection = Connection()
    connection.cursor.execute("""
      CREATE TABLE IF NOT EXISTS users (
        ID INT NOT NULL AUTO_INCREMENT,
        TELEGRAM_ID BIGINT UNIQUE,
        STRIPE_ID VARCHAR(255) UNIQUE,
        NAME VARCHAR(255) NOT NULL,
        EMAIL VARCHAR(255),
        PHONE VARCHAR(255),
        STATUS VARCHAR(255) NOT NULL,
        PRIMARY KEY (ID, TELEGRAM_ID)
      )
    """)

    print("Table users created")

# run the script
if __name__ == "__main__":
  dropAllTables()
  createUsersTable()

