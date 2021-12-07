from datetime import date , datetime, timedelta
import locale # подключаем форматы, но пока не указываем на какой (ниже)
'''date'''
today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday()) #weekday - метод нужны ()
print()

'''datetime'''
today2 = datetime.now() # в datetime так же  now == today
today3 = datetime.today()

print(today2, today3, sep="\n" )
print(today2)
print(today2.day)
print(today2.month)
print(today2.year)
print(today2.weekday())
print(today2.hour)
print(today2.minute)
print(today2.second)

days = ['пн','вт','ср','чт','пт','сб','вс',]
print(days[today2.weekday()])
print()
'''strptime - формат вывода времени '''
print(today2)
print(today2.strftime("%a"))
print(today2.strftime("%A"))
print(today2.strftime("%a %d %B %Y" ))
print()
''' locale - выбор формата страны для вывода времени'''
locale.setlocale(locale.LC_ALL, "ru_RU") # перешли на российский формат
print(today2.strftime("%A"))
print(today2.strftime("%a %d %B %Y" ))
print(f'Дата: {today2.strftime("%a - Ой тут что - %d %B %Y год(а)" )}')

print(today2.strftime("%c")) # универсальный формат вывода %с
print()
''' timedelta - разница во времени'''
print(today2.strftime("%c"))
d1 = today2 + timedelta(days=1, hours=1, minutes=10) # добавили время
print(d1.strftime("%c")) # добавленное время вывели в нужном нам формате