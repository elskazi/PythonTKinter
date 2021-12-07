''' Угадай чилсо Случайное и спросить хочешь еще раз '''
import random
my_num = random.randint(1,2)
count = 0
while True:
    num = input("Угадай число: ")
    if num.isdigit() == True : # isdigit -Вернёт True, если в строке цифры
        num = int(num) # input - возвращает строку, надо число странно что сверху прокатло
        count += 1
        if num > my_num:
            print(f"Меньше")
        elif num < my_num:
            print(f'Больше')
        else:
            print(f"Да, это число {num}, поптыток: {count} ")
            if input("Хотите еще раз, Д/Н: ") in ('Д','L','д','Y','y'): # сравниваем Да или другую кнопку нажал
                count = 0 # обнуляем счетчик
                my_num = random.randint(1, 2) # сбрасываем рандомное число

            else:
                print('Спасибо за сотрудничество!')
                break
    else:
        print('Не число')