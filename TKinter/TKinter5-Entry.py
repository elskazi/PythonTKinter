from tkinter import *

root = Tk()
root.title("Мое первое GUI приложение")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)
#root.config(bg="#000")
#root["bg"]= "red"

def add_str():
    e.insert(END, "HELLO")

def del_str():
    e.delete(0, END)

def get_str():
    l_text["text"] = e.get()


l = Label(root, text="Поле ввода")
l.pack()

e = Entry(root, )
e.insert(0, "Hello")
e.insert(END, " World")
e.pack()

btn_add = Button(root, text="ADD", command=add_str).pack()
btn_del_str = Button(root, text="DEL", command=del_str).pack()
btn_get_str = Button(root, text="GET", command=get_str).pack()

l_text = Label(root, bg="red" )
l_text.pack(fill=X)









root.mainloop()