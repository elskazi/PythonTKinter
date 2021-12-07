from tkinter import *

root = Tk()
root.title("Мое первое GUI приложение")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)


l_user = Label(root, text="Login: ", ).grid(row=0,column=0, padx = 10, pady=5,sticky=W)
e_user = Entry(root).grid(row=0, column=1,padx = 10, pady=5 , columnspan=2, sticky=W+E)

l_pass = Label(root, text="Password: ", ).grid(row=1,column=0, padx = 10, pady=5)
e_pass = Entry(root, show = "*").grid(row=1, column=1,padx = 10, columnspan=2 )

bnt_login = Button(root, text="Enter").grid(row=2, column=0, padx = 10, pady=5,sticky=W)
bnt_reg = Button(root, text="Reg").grid(row=2, column=1,)
bnt_for = Button(root, text="Forgot").grid(row=2, column=2, padx=10, )



root.mainloop()