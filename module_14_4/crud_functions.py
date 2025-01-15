import sqlite3

connection = sqlite3.connect("products.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
     title TEXT NOT NULL,
     description TEXT ,
     price INTEGER NOT NULL
    )
    ''')

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

# initiate_db()
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