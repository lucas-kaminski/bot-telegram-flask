from connection import Connection

from datetime import date

from dotenv import load_dotenv

load_dotenv()
import os

now = date.today()


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
        cursor.execute("DROP TABLE IF EXISTS adm_users")
        print("Table adm_users dropped")
    except:
        print("Error: unable to drop table adm_users")

    try:
        cursor.execute("DROP TABLE IF EXISTS vip_users")
        print("Table vip_users dropped")
    except:
        print("Error: unable to drop table vip_users")

    try:
        cursor.execute("DROP TABLE IF EXISTS products")
        print("Table products dropped")
    except:
        print("Error: unable to drop table products")

    try:
        cursor.execute("DROP TABLE IF EXISTS channels")
        print("Table channels dropped")
    except:
        print("Error: unable to drop table channels")

    try:
        cursor.execute("DROP TABLE IF EXISTS analises")
        print("Table analises dropped")
    except:
        print("Error: unable to drop table analises")

    try:
        cursor.execute("DROP TABLE IF EXISTS trades")
        print("Table trades dropped")
    except:
        print("Error: unable to drop table trades")

    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    connection.commit()
    connection.close()


def createUsersTable():
    connection = Connection()

    try:
        connection.cursor.execute(
            """
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
      """
        )
        print("Table users created")
    except:
        print("Error: unable to create table users")

    try:
        connection.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS adm_users(
          ID INT NOT NULL AUTO_INCREMENT,
          USER_ID INT NOT NULL UNIQUE,
          COUNTERSIGN VARCHAR(255) NOT NULL,
          POSITION VARCHAR(255) NOT NULL,
          ARCHIVE TEXT,
          PRIMARY KEY (ID),
          FOREIGN KEY (USER_ID) REFERENCES users(ID) ON DELETE CASCADE
        )
      """
        )
        connection.cursor.execute('ALTER TABLE adm_users MODIFY ARCHIVE TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin')
        print("Table adm_users created")
    except:
        print("Error: unable to create table adm_users")

    try:
        connection.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS vip_users (
          ID INT NOT NULL AUTO_INCREMENT,
          USER_ID INT NOT NULL,
          PRODUCT_ID INT NOT NULL,
          EXPIRATION DATE NOT NULL,
          STATUS VARCHAR(255) NOT NULL,
          PRIMARY KEY (ID)
        )
        """
        )
        print("Table vip_users created")
    except Exception as e:
        print(e)
        print("Error: unable to create table vip_users")

    try:
        connection.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS products (
          ID INT NOT NULL AUTO_INCREMENT,
          STRIPE_ID VARCHAR(255),
          NAME VARCHAR(255) NOT NULL,
          DESCRIPTION VARCHAR(255),
          PRICE FLOAT NOT NULL,
          VALIDITY_IN_MONTHS INT NOT NULL,
          PRIMARY KEY (ID)
        )
      """
        )
        print("Table products created")
    except:
        print("Error: unable to create table products")

    try:
        connection.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS channels (
          ID INT NOT NULL AUTO_INCREMENT,
          TELEGRAM_ID BIGINT UNIQUE,
          NAME VARCHAR(255) NOT NULL,
          PRIMARY KEY (ID)
        )
      """
        )
        print("Table channels created")
    except:
        print("Error: unable to create table channels")

    try:
        connection.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS analises (
          ID INT NOT NULL AUTO_INCREMENT,
          TITLE VARCHAR(255),
          BODY TEXT NOT NULL,
          LINK VARCHAR(255),
          AUTHOR_ID INT NOT NULL,
          UPDATED_AT DATETIME NOT NULL,
          EDITED_AT DATETIME NOT NULL,
          PRIMARY KEY (ID),
          FOREIGN KEY (AUTHOR_ID) REFERENCES adm_users(ID) ON DELETE CASCADE
        )
        """
        )
        print("Table analises created")
    except Exception as e:
        print(e)
        print("Error: unable to create table analises")

    try:
        connection.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS trades (
          ID INT NOT NULL AUTO_INCREMENT,
          SYMBOL VARCHAR(255) NOT NULL,
          CREATED_BY INT NOT NULL,
          UPDATED_AT DATETIME NOT NULL,
          EDITED_AT DATETIME NOT NULL,
          PRIMARY KEY (ID),
          FOREIGN KEY (CREATED_BY) REFERENCES adm_users(ID) ON DELETE CASCADE
        )
        """
        )
        print("Table trades created")
    except:
        print("Error: unable to create table trades")

    connection.commit()
    connection.close()


def insertData():
    connection = Connection()

    telegram_id = os.environ.get("CHAT_ID_TELEGRAM_DEVELOPER")
    connection.cursor.execute(
        """
        INSERT INTO channels (TELEGRAM_ID, NAME) VALUES
        VALUES (%s, 'TESTE')
        """, (telegram_id,)
    )

    telegram_id = os.environ.get("CHAT_ID_TELEGRAM_DEVELOPER")
    name = "Teste"
    email = "teste@teste.com.br"
    phone = "419999999999"
    status = "completed"

    connection.cursor.execute(
        """
    INSERT INTO users (ID, TELEGRAM_ID, NAME, EMAIL, PHONE, STATUS)
    VALUES (%s, %s, %s, %s, %s, %s)
  """,
        ('1', telegram_id, name, email, phone, status),
    )
    print("User inserted")

    position = "ADMIN"
    countersign = "TESTE"
    connection.cursor.execute(
        """
    INSERT INTO adm_users (ID, USER_ID, COUNTERSIGN, POSITION)
    VALUES (%s, %s, %s, %s)
  """,
        ('1', '1', countersign, position),
    )
    print("Admin user inserted")

    connection.cursor.execute(
        """
    INSERT INTO products (NAME, DESCRIPTION, PRICE, VALIDITY_IN_MONTHS) VALUES
    ('VIP MENSAL [VIP 249]', '', 249.90, 1),
    ('VIP TRIMESTRAL [VIP 229]', '', 229.90, 3),
    ('VIP SEMESTRAL [VIP 189]', '', 189.90, 6),
    ('VIP [VIP 689]', '', 689.70, 3),
    ('VIP [VIP 1134]', '', 1134.40, 6)
  """
    )
    print("Products inserted")

    title = "Análise Bitcoin"
    body = """
  Boa tarde, pessoal!

Realmente fomos testar os U$ 29.000 dólares hein? E além de testar o U$ 29.000 dólares, também tocamos levemente na nossa LTB (Linha de Tendência de Baixa) rompida no dia 29 de Maio e voltamos a subir. O mercado está bem volátil esses últimos dias por isso devemos sempre nos manter atentos ao gráfico.

No gráfico de 4 horas, o preço volta a ficar abaixo das medias, porém agora as medias começam a ficar mais juntas e não tão separadas, somente as medias de 200 períodos (linha verde e linha laranja) que estão mais acima e apresentam uma forte resistência ao preço. No gráfico diário, no dia de ontem quase entregamos toda a subida do dia 30 de Maio, mas os compradores começaram a reagir antes que isso acontecesse. Porém agora estamos abaixo da EMA de 20 períodos (linha vermelha) novamente, apresentando mais uma vez a resistência ao preço.

Não tem muito o que fazer nesse momento, apesar da turbulência, ainda estamos em uma área de lateralização, se formos perceber estamos andando de lado nessa zona desde o começo de Maio praticamente. E ainda temos muito ruído do mercado tradicional que também não está desempenhando bem nos últimos dias e o FED cada vez mais pensando em aumentar a taxa de juros. Momento complicado, mas que passará, só termos calma e paciência. Novamente, cautela ao operar nesse período! Podemos ainda ir testar os U$ 32.000 dólares (forte resistência), por isso cuidado!

Sempre gerenciem o risco de vocês de modo adequado, nunca coloquem todo o capital em uma só operação e nem em uma criptomoeda só.

Nosso suporte mais importante está na região dos U$ 29.000-25.000 dólares. Nossa resistência agora está em U$ 32.000 dólares e U$ 35.000 dólares.

Lembrando que o mercado das criptomoedas é um mercado extremamente volátil, essa é só uma opinião técnica.
"""
    link = "https://www.tradingview.com/x/qxjORn7l/"
    updated_at = now
    edited_at = now
    connection.cursor.execute(
        """
    INSERT INTO analises (TITLE, BODY, LINK, AUTHOR_ID, UPDATED_AT, EDITED_AT) VALUES (%s, %s, %s, %s, %s, %s)
    """,
        (title, body, link, '1', updated_at, edited_at),
    )
    print("Analises inserted")

    connection.commit()
    connection.close()


# run the script
if __name__ == "__main__":
    dropAllTables()
    createUsersTable()
    insertData()

    print("Finalizado, agora execute as sincronizações")
