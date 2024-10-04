# task_manager/database.py
import sqlite3

def connect():
    """Connects to the SQLite database."""
    return sqlite3.connect('tasks.db')

def create_tables():
    """Creates the users and tasks tables."""
    conn = connect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    due_date DATE NOT NULL,
                    status TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )''')
    conn.commit()
    conn.close()
