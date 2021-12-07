from tkinter import *

root = Tk()
root.title("Мое первое GUI приложение")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)
#root.config(bg="#000")
#root["bg"]= "red"



# def Red():
#     e.delete(0, END)
#     e.insert(END, "ff0000")
#     #e.xview(5)
#     l["text"] = "Красный"
# def Orange():
#     e.delete(0, END)
#     e.insert(END, "ff7d00")
#     l["text"] = "Оранжевый"
# def Yellow():
#     e.delete(0, END)
#     e.insert(END, "ffff00")
#     l["text"] = "Желтый"
# def Green():
#     e.delete(0, END)
#     e.insert(END, "00ff00")
#     l["text"] = "Зеленый"
# def Blue():
#     e.delete(0, END)
#     e.insert(END, "007dff")
#     l["text"] = "Голубой"
# def DarkBlue():
#     e.delete(0, END)
#     e.insert(END, "0000ff")
#     l["text"] = "Синий"
# def Purple():
#     e.delete(0, END)
#     e.insert(END, "7d00ff")
#     l["text"] = "Фиолеторый"


l = Label(root, text="цвет", anchor="center")
l.pack()
e = Entry(root, justify='center' )
e.pack()

colors = {
'#ff0000': 'Красный',
'#ff7d00': 'Оранжевый',
'#ffff00': 'Желтый',
'#00ff00': 'Зеленый',
'#007dff': 'Голубой',
'#0000ff': 'Синий',
'#7d00ff': 'Фиолеторый',
}

def get_color(text_color, hex_color):
    e.delete(0, END)
    e.insert(END, hex_color)
    l["text"] = text_color

for k, v in colors.items():
    Button(root, command=lambda text=v, hex=k: get_color(text, hex), bg=k).pack(fill=X)

# btn_Red = Button(root, command=lambda: get_color('Красный', "ff0000"),  bg="#ff0000")
# btn_Red.pack(fill=X)
# btn_Orange = Button(root, command=lambda: get_color('Оранжевый', "ff7d00"),  bg="#ff7d00" )
# btn_Orange.pack(fill=X)
# btn_Yellow = Button(root, command=lambda: get_color('Желтый', "ffff00"),  bg="#ffff00" )
# btn_Yellow.pack(fill=X)
# btn_Green = Button(root, command=lambda: get_color('Зеленый', "00ff00"),  bg="#00ff00" )
# btn_Green.pack(fill=X)
# btn_Blue = Button(root, command=lambda: get_color('Голубой', "007dff"),  bg="#007dff" )
# btn_Blue.pack(fill=X)
# btn_DarkBlue = Button(root, command=lambda: get_color('Синий', "0000ff"),  bg="#0000ff" )
# btn_DarkBlue.pack(fill=X)
# btn_Purple = Button(root, command=lambda: get_color('Фиолеторый', "7d00ff"),  bg="#7d00ff" )
# btn_Purple.pack(fill=X)

root.mainloop()