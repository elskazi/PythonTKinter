from tkinter import *


root = Tk()
root.title("Text & Scrollbar")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)

f_menu = Frame(root, bg="#1F252A", height=40)
f_text = Frame(root)

f_menu.pack(fill=X)
f_text.pack(fill=BOTH, expand = 1)

l_menu = Label(f_menu, text= "Menu", bg="#2B3239", fg= "#C6DEC1", font="Arial 12")
l_menu.place(x=10,y=10)

def add_str():
    text_o.insert('2.4', "HELLO")
def del_str():
    #text_o.delete('2.4', '2.10')
    text_o.delete('1.0', END)
def get_str():
   print(text_o.get("1.0", END))

btn_add = Button(root, text="ADD", command=add_str).place(x=50,y=10)
btn_del_str = Button(root, text="DEL", command=del_str).place(x=90,y=10)
btn_get_str = Button(root, text="GET", command=get_str).place(x=140,y=10)


text_o = Text(f_text, bg="#343D46", fg= "#C6DEC1", padx=10, pady=10, font="Arial 12", wrap=WORD,
              insertbackground="orange", selectbackground="blue", spacing3=10, width=10 )
text_o.pack(fill=BOTH, expand = 1, side=LEFT)

scroll = Scrollbar(f_text, command=text_o.yview)
scroll.pack(fill=Y, side=LEFT )
#print(text_o['width'], text_o['height']) # ширина 800 и не будет видно стролаа, ставим ширину в текстовой областе менбше 30

text_o.config(yscrollcommand=scroll.set)

root.mainloop()