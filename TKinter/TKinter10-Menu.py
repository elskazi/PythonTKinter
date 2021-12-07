from tkinter import *


root = Tk()
root.title("Text & Scrollbar")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)

# f_menu = Frame(root, bg="#1F252A", height=40)
# f_menu.pack(fill=X)

main_menu = Menu(root)
root.config(menu=main_menu)

# main_menu.add_command(label='File')
# main_menu.add_command(label='About')

def about_programm():
    print("Привет ")

#File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть")
file_menu.add_command(label="Сохранить")
file_menu.add_separator()
file_menu.add_command(label="Выход")
main_menu.add_cascade(label="Файл", menu=file_menu )

#About
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0 )
help_menu_sub.add_command(label="Перейти на сайт")
help_menu_sub.add_command(label="Локальная справкап")
help_menu.add_cascade(label="Помощь", menu=help_menu_sub)
help_menu.add_command(label="О программе", command = about_programm)
main_menu.add_cascade(label="Справка", menu=help_menu )



f_text = Frame(root)
f_text.pack(fill=BOTH, expand = 1)

# l_menu = Label(f_menu, text= "Menu", bg="#2B3239", fg= "#C6DEC1", font="Arial 12")
# l_menu.place(x=10,y=10)


text_o = Text(f_text, bg="#343D46", fg= "#C6DEC1", padx=10, pady=10, font="Arial 12", wrap=WORD,
              insertbackground="orange", selectbackground="blue", spacing3=10, width=10 )
text_o.pack(fill=BOTH, expand = 1, side=LEFT)

scroll = Scrollbar(f_text, command=text_o.yview)
scroll.pack(fill=Y, side=LEFT )
#print(text_o['width'], text_o['height']) # ширина 800 и не будет видно стролаа, ставим ширину в текстовой областе менбше 30

text_o.config(yscrollcommand=scroll.set)

root.mainloop()