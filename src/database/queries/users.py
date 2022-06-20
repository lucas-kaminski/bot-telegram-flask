from database.connection import Connection

def selectUser(id = None, telegram_id = None, stripe_id = None):
  connection = Connection()
  cursor = connection.cursor

  if id is not None:
    cursor.execute(f"SELECT * FROM users WHERE ID = {id}")
    user = cursor.fetchone()
  elif telegram_id is not None:
    cursor.execute(f"SELECT * FROM users WHERE TELEGRAM_ID = {telegram_id}")
    user = cursor.fetchone()
  elif stripe_id is not None:
    cursor.execute(f"SELECT * FROM users WHERE STRIPE_ID = {stripe_id}")
    user = cursor.fetchone()
  else:
    user = None

  connection.close()
  return user

def insertUser(chat_id, name, status):
  connection = Connection()
  cursor = connection.cursor
  cursor.execute(f"INSERT INTO users (TELEGRAM_ID, NAME, STATUS) VALUES ('{chat_id}', '{name}', '{status}')")
  connection.commit()
  connection.close()
  return selectUser(telegram_id=chat_id)

def updateUser(id, telegram_id = None, stripe_id = None, name = None, email = None, phone = None, status = None):
  params = {"telegram_id": telegram_id, "stripe_id": stripe_id, "name": name, "email": email, "phone": phone, "status": status}
  connection = Connection()
  cursor = connection.cursor

  sql = f"UPDATE users SET "
  for key, value in params.items():
    if value is not None:
      sql += f"{key} = '{value}', "

  sql = sql[:-2]
  sql += f" WHERE ID = {id}"

  print(sql)
  cursor.execute(sql)
  connection.commit()
  connection.close()
  return selectUser(id=id)
