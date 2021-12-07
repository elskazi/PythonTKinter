from tkinter import *
from tkinter import ttk
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
def click():
    print("Нажал")
'''Конец Функция при нажатии'''

'''Кнопка(и)'''
btn = Button(root, text="Start\ngo", command=click, width=0, height= 0,  padx=40, pady=20, font = "Arial 14", justify='left')
btn.pack()
btn2 = ttk.Button(root, text="Start", command=click, width=15)
btn2.pack()
'''Конец Кнопка'''

'''Вывод на укран'''
root.mainloop()
'''Конец Вывод на ужран'''