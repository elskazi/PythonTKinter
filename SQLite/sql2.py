import sqlite3

db = sqlite3.connect("test_db.sqlite") # подключение
cursor = db.cursor()  # курсов, обязательный обьект для создания запросов

''' Вставляем данные в таблицу'''
# cursor.execute ('''CREATE TABLE IF NOT EXIST users
# (id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# email TEXT NOT NULL UNIQUE
# )''') # созадать таблицу Юзерс с полями ИД, имяБ емайл

# cursor.execute("INSERT INTO users (name, email) VALUES ('Bugaga gaga', 'bugaga@gmail.com')") # создать запрос
# cursor.execute("INSERT INTO users (name, email) VALUES ('Ваильев Вася', 'vas@gmail.com')") # создать запрос

# cursor.executescript('''
# INSERT INTO users (name, email) VALUES ('John Jon', 'Jon@gmail.com');
# INSERT INTO users (name, email) VALUES ('Yansia yan', 'yan@gmail.com');
# ''')  # вствка многих плей , ставить точку запитой на конце

users = [
    ("users 1 ", "user1@user.com"),
    ("users 2 ", "user2@user.com"),
    ("users 3 ", "user3@user.com"),
]
cursor.executemany("INSERT INTO users (name, email) VALUES (?,?)" , users)  # вставка не изветного количества данных


db.commit() # отправить данные


db.close() # закрыть базу