from connection import Connection

def dropAllTables():
    connection = Connection()
    cursor = connection.cursor

    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    try:
      cursor.execute("DROP TABLE IF EXISTS users")
      print("Table users dropped")
    except:
      print("Error: unable to drop table users")

    try:
      cursor.execute("DROP TABLE IF EXISTS channels")
      print("Table channels dropped")
    except:
      print("Error: unable to drop table channels")

    try:
      cursor.execute("DROP TABLE IF EXISTS products")
      print("Table products dropped")
    except:
      print("Error: unable to drop table products")

    try:
      cursor.execute("DROP TABLE IF EXISTS vip_users")
      print("Table vip_users dropped")
    except:
      print("Error: unable to drop table vip_users")

    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    connection.commit()
    connection.close()

def createUsersTable():
    connection = Connection()
    try:
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
    except:
      print("Error: unable to create table users")

    try:
      connection.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
          ID INT NOT NULL AUTO_INCREMENT,
          STRIPE_ID VARCHAR(255),
          NAME VARCHAR(255) NOT NULL,
          DESCRIPTION VARCHAR(255),
          PRICE FLOAT NOT NULL,
          VALIDITY_IN_MONTHS INT NOT NULL,
          PRIMARY KEY (ID)
        )
      """)
      print("Table products created")
    except:
      print("Error: unable to create table products")

    try:
      connection.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vip_users (
          ID INT NOT NULL AUTO_INCREMENT,
          USER_ID INT NOT NULL,
          PRODUCT_ID INT NOT NULL,
          EXPIRATION DATE NOT NULL,
          STATUS VARCHAR(255) NOT NULL,
          PRIMARY KEY (ID),
          FOREIGN KEY (USER_ID) REFERENCES users(ID) ON DELETE CASCADE,
          FOREIGN KEY (PRODUCT_ID) REFERENCES products(ID) ON DELETE CASCADE
        )
        """)
      print("Table vip_users created")
    except:
      print("Error: unable to create table vip_users")

    try:
      connection.cursor.execute("""
        CREATE TABLE IF NOT EXISTS channels (
          ID INT NOT NULL AUTO_INCREMENT,
          TELEGRAM_ID BIGINT UNIQUE,
          NAME VARCHAR(255) NOT NULL,
          PRIMARY KEY (ID)
        )
      """)
      print("Table channels created")
    except:
      print("Error: unable to create table channels")

    connection.commit()
    connection.close()


def insertData():
  connection = Connection()
  connection.cursor.execute("""
    INSERT INTO products (NAME, DESCRIPTION, PRICE, VALIDITY_IN_MONTHS) VALUES
    ('VIP MENSAL [VIP 249]', '', 249.90, 1),
    ('VIP TRIMESTRAL [VIP 229]', '', 229.90, 3),
    ('VIP SEMESTRAL [VIP 189]', '', 189.90, 6),
    ('VIP [VIP 689]', '', 689.70, 3),
    ('VIP [VIP 1134]', '', 1134.40, 6)
  """)
  print("Products inserted")

  connection.commit()
  connection.close()

# run the script
if __name__ == "__main__":
  dropAllTables()
  createUsersTable()
  insertData()

  print("Finalizado, agora execute as sincronizações")

