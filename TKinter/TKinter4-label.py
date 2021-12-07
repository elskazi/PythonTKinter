from tkinter import *

root = Tk()
root.title("Мое первое GUI приложение")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)
#root.config(bg="#000")
#root["bg"]= "red"

''' играемся с расположением текста в лайбле'''
l = Label(root, text = "строке 1\nТекст в строке 2\nТекст в строке 3\nТекст в строке 4\nТекст в строке 5 ",
          fg = "#355", justify='left', bg = "#aaa" ,  width=33, height= 10, anchor="se")
l.pack()
''' Изображение в лайбле'''
img = PhotoImage(file="ico.png")
l_logo = Label(root, image=img)
l_logo.pack()


root.mainloop()