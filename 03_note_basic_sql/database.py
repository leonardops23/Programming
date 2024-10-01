import sqlite3
# config with sqllite

def connect():
    return sqlite3.connect('notes.db')


def create_table():
    conn = connect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              content TEXT NOT NULL,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              )''')

    conn.commit()
    conn.close()
