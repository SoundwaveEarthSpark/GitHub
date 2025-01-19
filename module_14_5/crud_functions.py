import sqlite3

connection = sqlite3.connect("products.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
 id INTEGER PRIMARY KEY,
 username TEXT NOT NULL,
 email TEXT NOT NULL,
 age INTEGER NOT NULL,
 balance INTEGER NOT NULL
)
''')

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                    (username, email, age, 1000))
    connection.commit()

def is_included(username):
    user = cursor.execute(('SELECT * FROM Users WHERE username = ?'),(username, )).fetchone()
    if user is None:
        return False
    else:
        return True


#initiate_db()
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                 ('Кальций', 'Описание1', 100))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                ('Железо с витамином С', 'Описание2', 200))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                ('Йод', 'Описание3', 300))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                ('Магний с B6', 'Описание4', 400))
#
# connection.commit()
#
# connection.close()