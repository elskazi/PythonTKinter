# ''' Функция в степень'''
# def get_square(num):
#     return num ** 2
#
# print(get_square(2))
# ''' Функция в степень через lambda ( не стандарт) '''
# get_square = lambda num: num ** 2
# print(get_square(2)) # 4
#
# '''Функция в степень через lambda '''
# print((lambda num: num ** 2) (10)) #100

# '''Функция список * 2 '''
# l = [1,2,3] # надо *2
# def get_double(l):
#     return [i * 2 for i in l]  # обычный вариант
# print(get_double(l)) # [2, 4, 6]

'''Функция список * 2 через lambda'''
l = [1,2,3] # надо *2
def get_double(l):
    return list(map(lambda num: num * 2 , l)) # map применяет функцию к каждому из элементов
print(get_double(l)) # [2, 4, 6]