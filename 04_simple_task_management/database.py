import sqlite3

"""

"""

def connect():
    return sqlite3.connect('tasks.db')


def create_table():
    cnn = connect()
    c = cnn.cursor()
    c.execute('''CREATE TABLE IF NOT EXITS users (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL UNIQUE,
              password TEXT NOT NULL,
              )''')
    c.execute('''CREATE TABLE IF NOT EXISTS notes (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER,
              title TEXT NOT NULL,
              priority TEXT NOT NULL,
              due_date DATE NOT NULL,
              status TEXT NOT NULL,
              FOREIGN KEY (user_id) REFERENCES users (id)
              )''')
    cnn.commit()
    cnn.close()
