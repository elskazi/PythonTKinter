import sqlite3





db = sqlite3.connect("test_db.sqlite") # подключение
cursor = db.cursor()  # курсов, обязательный обьект для создания запросов

''' Получаем данные из таблицы '''
email = "bugaga@gmail.com"

# cursor.execute(f" SELECT * FROM users WHERE email = '{email}' ") # не рекомндуемый способ f
# res = cursor.fetchone() # fetchone - только 1 ответ
# print(res)
# print(res[1])

''' Правильный вариант '''
#cursor.execute("SELECT * FROM users WHERE email = ? ", (email, )) # запятею обязательно что б был кортеж
#cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (email, "Yansia yan")) # то или то
#cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name" , {'email': email, 'name': 'Yansia yan' }) # через словарь

cursor.execute("SELECT * FROM users ")
res = cursor.fetchall()
print(res)

# for user in res:
#     print(user[1], user[2])


#print(res[1])




db.close() # закрыть базу