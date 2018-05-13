import sqlite3


# Если не было, создаем на сервере БД с необходимыми таблицами.
def db_initiation():
    conn = sqlite3.connect('../twocups.db')
    conn.cursor()

    conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      login TEXT UNIQUE,
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
      id_contact INTEGER REFERENCES users (id),
      UNIQUE (id_user, id_contact)
    );
    ''')

    conn.commit()
    # conn.close()


if __name__ == '__main__':
    db_initiation()
