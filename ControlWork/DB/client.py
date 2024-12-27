import sqlite3


connect = sqlite3.connect('clients.db')
cursor = connect.cursor()
def create_db():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                userid INTEGER PRIMARY KEY AUTOINCREMENT,
                fio VARCHAR(100) NOT NULL,
                age INTEGER NOT NULL,
                hobby TEXT
            )
        ''')
    connect.commit()
create_db()
def add_client(fio, age, hobby=""):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio, age, hobby))
    connect.commit()
    print(f"Пользователь {fio} добавлен")
add_client('Геннадий Головкин', 33, 'бокс')
add_client('Роберт Фищер', 27, 'шахматы')
add_client('Макс Ферстапен', 28, 'гонки')
add_client('Ип-Ман', 35, 'кунг-фу')
add_client('Арнольд ', 33, 'зал')
def get_all_client():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        print("Список всех пользователей:")
        for user in users:
            print(f"ID: {user[0]}, FIO: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}")
    else:
        print("Список пользователей пуст")
get_all_client()
def update_clietn_name(user_id, fio):
    cursor.execute('UPDATE users SET fio = ? WHERE userid = ?', (fio, user_id))
    connect.commit()
    print(f"ФИО пользователя с ID {user_id} обновлено")
update_clietn_name(2, "Магнус Карлсон")
def delete_client(user_id):
    cursor.execute('DELETE FROM users WHERE userid = ?', (user_id,))
    connect.commit()
    print(f"Пользователь с ID {user_id} удален")
delete_client(5)
get_all_client()
connect.close()