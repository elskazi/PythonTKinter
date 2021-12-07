from tkinter import *

import time

root = Tk()
root.title("Время")

def tick():
    watch.after(200, tick)
    watch['text'] = time.strftime("%H:%M:%S")


watch = Label(root, font= "Sans 52")
watch.pack(ipady=10,ipadx=10)
tick()


root.mainloop()