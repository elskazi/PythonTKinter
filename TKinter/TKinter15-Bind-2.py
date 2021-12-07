from tkinter import *


root = Tk()
root.title("Bind")
root.geometry("500x300+300+200")

def f_event(event, key):
    print(event, key)

e = Entry(root, justify=CENTER, font="Sans 15")
e.pack(fill=X, expand=1, padx=10, pady=10, ipady=10, ipadx=10)
e.bind("<Button-1>", lambda event, key="Жмякнули левой": f_event(event,key))
e.bind("<Button-2>", lambda event, key="Жмякнули средней": f_event(event,key))
e.bind("<Button-3>", lambda event, key="Жмякнули правой": f_event(event,key))
e.bind("<FocusIn>", lambda event, key="Фокус в ": f_event(event,key))
root.mainloop()