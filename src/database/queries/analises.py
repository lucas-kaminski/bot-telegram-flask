from database.connection import Connection

def selectLastAnalise():
  connection = Connection()
  cursor = connection.cursor

  cursor.execute('SELECT * FROM analises ORDER BY ID DESC LIMIT 1')
  analise = cursor.fetchone()

  connection.close()
  return analise
