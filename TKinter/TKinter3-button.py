from tkinter import *
import time
'''Свойства окна '''
root = Tk()
root.title("Мое первое GUI приложение")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)
#root.config(bg="#000")
#root["bg"]= "red"
'''Конец Свойства окна '''

'''Функция при нажатии кнопки'''
def check_time():
    t= time.strftime("%H:%M:%S")
    btn["text"] = t
    #print(t)


clicks = 0
def counter():
    global clicks
    clicks+=1
    root.title(clicks) # жмякаем и в заголовку + 1

x = 10
y =2
def summaa():
    suma = x+y
    btn_sum["text"] = suma
def vichets():
    vichet = x-y
    btn_vichet["text"] = vichet
def ymnojenie():
    ymnojen = x*y
    btn_ymnojenie["text"] = ymnojen
def delenie():
    delen = x/y
    btn_delenie["text"] = delen

'''Конец Функция при нажатии'''

'''Кнопка(и)'''
btn = Button(root, text="Время", command=check_time, width=0, height= 0,  padx=40, pady=20, font = "Arial 14", justify='left')
btn.pack()
btn_count = Button(root, text="Счетчик", command=counter, width=0, height= 0,  padx=40, pady=20, font = "Arial 14")
btn_count.pack()
btn_sum = Button(root, text="Сложение", command=summaa,  padx=40, pady=20, )
btn_sum.pack()
btn_vichet = Button(root, text="Вычитание", command=vichets,  padx=40, pady=20, )
btn_vichet.pack()
btn_ymnojenie = Button(root, text="Умножение", command=ymnojenie,  padx=40, pady=20, )
btn_ymnojenie.pack()
btn_delenie = Button(root, text="Деление", command=delenie,  padx=40, pady=20, )
btn_delenie.pack()

'''Конец Кнопка'''

'''Вывод на укран'''
root.mainloop()
'''Конец Вывод на ужран'''