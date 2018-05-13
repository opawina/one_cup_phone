import sqlite3
import sqlalchemy
import datetime
import os

# Если не было, создаем на сервере БД с необходимыми таблицами.
def db_initiation():
    conn = sqlite3.connect('twocups.db')
    conn.cursor()

    conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE,
      date TEXT,
      host TEXT 
    );
    ''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS users_history (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      id_user INTEGER REFERENCES users (id),
      message TEXT,
      date TEXT,
      id_chat INTEGER
    );
    ''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS users_list_contacts (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      id_user INTEGER REFERENCES users (id),
      id_contact INTEGER REFERENCES users (id)
    );
    ''')

    conn.commit()
    conn.close()
