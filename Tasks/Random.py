from random import random,randint,randrange
''' random() - генерация от 0 до 1  , 0 входит(но не реально) , 1 не входит '''
# print(random())
#
# ''' Рандоманя генерация 10 тыщ раз  в а - самое наименьшее запишем, в б - самое наибольшее'''
# a = 0.1
# b = 0.9
# i = 0
# while i < 100000:
#     n = random()
#     if n < a:
#         a = n
#     elif n > b:
#         b = n
#     i += 1
#
# print("%.16f" %a)
# print(b)
#
# '''При использовании ИНТ верхняя граница не будет входить в диапозон '''
# '''При использовании ROUND верхняя граница будет входить в диапозон '''
#
# ''' Если надо сгенерить целое цисло то умножаем '''
# print(int(random()*100))
#
# ''' Если надо сгенерить целое трех значное число от 100 до 999'''
# print(int(random()*900+100))
#
# ''' от 6 до 10'''
# print(int(random()*(10-6)+6))
#
# ''' от -2 до 2 '''
# x = random()
# print(int(x * (2 - -2) + -2))  # можно +  далее -
# print(round(x * (2 +2) -2))  # можно +  далее -
#
# ''' randint генерация целых чисел, всегда 2 аргумента - верхняя и нижняя граница, границы входят в диапозон'''
# print(randint(5,10))

''' randrange генерация целых чисел, если 1, то от 0 до этого значения,  если 2 аргумента то вротой не входит в диапозон 
можно передавать 3й аргумент это шаг'''
print(randrange(2)) # 0 или 1
print(randrange(1, 2)) # всегда 1, вторй арг не входит
print(randrange(1, 10, 3)) # шаг=3, ответы может быть только 1, 4, 7

