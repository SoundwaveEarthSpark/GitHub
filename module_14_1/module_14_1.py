import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
 id INTEGER PRIMARY KEY,
 username TEXT NOT NULL,
 email TEXT NOT NULL,
 age INTEGER,
 balance INTEGER NOT NULL
)
''')

for i in range (1,11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))


cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 = 0", (500,))
j = 1
while j < 12:
    cursor.execute('DELETE FROM Users WHERE id = ?', (j,))
    j = j + 3

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
records = cursor.fetchall()
for r in records:
    username, email, age, balance = r
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

connection.commit()
