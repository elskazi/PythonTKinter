from tkinter import *


root = Tk()
root.title("Квадрат Малевича")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)

l1 = Label(root,  bg="black", fg = "#fff",  )
l1.place( relx= 0.1,rely= 0.1 , relheight= 0.8, relwidth= 0.8,  ) # запилить обьект по центру
l2 = Label(root,  bg="red", fg = "#fff",  )
l2.place( relx= 0.5,rely= 0.5 , relheight= 0.6, relwidth= 0.6, anchor="c" )# запилить обьект по центру, anchor - точка отсчета



root.mainloop()