
''' Нужно список умножить на 2'''
i = [1,"2",3]
''' Вариант 1, функция '''
def f(i):
    return [l * 2 for l in i]
print(f(i))
''' Вариант 2, вытащили умножение в отдельную функцию '''
def f2(i):
    def get_mult(x):
        return x * 2
    return [get_mult(l) for l in i]
print(f2(i))

''' Нужно список умножить на 2 и если одно значение строка, ее надо убрать'''
i = [1,"2",3]
def f3(i):
    def get_mult(x):
        if isinstance( x, int):  #  isinstance - проверяет переменную x - число ли это int
            return x * 2
    return [get_mult(l) for l in i if get_mult(l)] # если убрать if get_mult(l) строковое значение будет NONE
print(f3(i))


def f4(i):
    def get_mult(x):
        return x * 2
    return list(map(get_mult, i))
print(f4(i))