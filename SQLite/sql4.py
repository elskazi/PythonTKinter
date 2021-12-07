import sqlite3
''' Получить словарь'''
def dict_factory (cur,row):
    d = {}
    for idx , col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d

db = sqlite3.connect("test_db.sqlite") # подключение
db.row_factory = dict_factory # Получить словарь
cursor = db.cursor()  # курсов, обязательный обьект для создания запросов

cursor.execute("SELECT * FROM users ")
res = cursor.fetchall()
print(res) # прилетел словарь

for user in res:
    print(user["name"], user["email"]) # обращаемся по ключам