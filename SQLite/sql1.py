import sqlite3

db = sqlite3.connect("test_db.sqlite") # подключение
cursor = db.cursor()  # курсов, обязательный обьект для создания запросов

cursor.execute ('''CREATE TABLE users
(id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL UNIQUE
)''') # созадать таблицу Юзерс с полями ИД, имяБ емайл

db.close() # закрыть базу