from tkinter import *


root = Tk()
root.title("Bind")
root.geometry("500x300+300+200")

def f_event(event):
    print(event)


l = Label(root, bg="red"  )
l.pack(fill=X, expand=1)
l.bind("<Button-1>",  f_event)

root.mainloop()