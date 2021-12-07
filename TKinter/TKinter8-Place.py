from tkinter import *


root = Tk()
root.title("Мое первое GUI приложение")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)

l1 = Label(root, text = "Hello world", bg="#3498db", fg = "#fff", padx=200, pady =100  )
l1.place( relx= 0.5, rely= 0.5, anchor="c" ) # запилить обьект по центру, anchor - точка отсчета

btn1 = Button(root, text="Button1", bg = "red", padx=20, pady =10 )
btn1.place(x=0,y=0)
btn2 = Button(root, text="Button2", bg = "red", padx=20, pady =10)
btn2.place(relx= 0.5, rely= 0.5, anchor="c" )
btn2 = Button(root, text="Button2", bg = "blue", fg = "white", padx=20, pady =10)
btn2.place(relx= 1, rely= 1, anchor="se" )

root.mainloop()