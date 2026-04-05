# Database initialization script

import sqlite3

def init_db():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, contact TEXT)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()