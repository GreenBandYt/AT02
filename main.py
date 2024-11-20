import sqlite3

def init_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        age INTEGER
    )
    ''')

    return conn

def add_user(conn, username, age):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, age) VALUES (?, ?)', (username, age))
    conn.commit()

def get_users(conn, username):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    return cursor.fetchone()