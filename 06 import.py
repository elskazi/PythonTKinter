
print(__name__)
''' Импортировать весь файл(модуль) '''
import libs
print (libs.get_count('hello','l'))
print(libs.get_len("hello world"))

# ''' Импортировать весь файл(модуль) с использованием псевдонима '''
# import libs as l
# print (l.get_count('hello','l'))
# print(l.get_len("hello world"))
#
# ''' Импортировать файл(модуль) с определенными функциями и с использованием псевдонима '''
# from libs import get_count as c, get_len as l
# print (c('hello','l'))
# print(l("hello world"))
#
# ''' Импортировать файл(модуль) с определенными функциями '''
# from libs import get_count, get_len
# print (get_count('hello','l'))
# print(get_len("hello world"))