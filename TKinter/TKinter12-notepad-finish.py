from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Text & Scrollbar")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)

main_menu = Menu(root)
root.config(menu=main_menu)

def about_programm():
    messagebox.showinfo(title="Программа блокнот", message="Мой первый блокнот версии 0.1")

def quittt():
    answer = messagebox.askokcancel(title="Выход", message="Закрыть программу?" )
    #print(answer)
    if answer:
        root.destroy() # закрытие нашего рут окна

def open_file():
    file_path = filedialog.askopenfilename(title="Выбор файла", filetypes=(("Тестовые документы", "*.txt"),
                                                                           ("Все файлы (*.*)", "*.*")))
    if file_path:
        text_o.delete("1.0", END)
        text_o.insert("1.0", open(file_path, encoding="utf=8").read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Сохранить", filetypes=(("Тестовые документы", "*.txt"),
                                                                           ("Все файлы (*.*)", "*.*")))
    f = open(file_path, "w", encoding="utf=8"  )
    text = text_o.get("1.0", END)
    f.write(text)
    f.close()



def changt_theme(theme):
    text_o["bg"] = theme_colors[theme]["text_bg"],
    text_o["fg"] = theme_colors[theme]["text_fg"],
    text_o["insertbackground"] = theme_colors[theme]["cursor"],
    text_o["selectbackground"] = theme_colors[theme]["secelt_bg"],
    #print(theme)

#File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть",command=open_file)
file_menu.add_command(label="Сохранить как",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход",command=quittt )
main_menu.add_cascade(label="Файл", menu=file_menu )

#theme
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0 )
theme_menu_sub.add_command(label="Белая", command = lambda : changt_theme('light'))
theme_menu_sub.add_command(label="Темная", command = lambda : changt_theme('dark'))
theme_menu.add_cascade(label="Тема", menu=theme_menu_sub)
theme_menu.add_command(label="О программе", command = about_programm)
main_menu.add_cascade(label="Разное", menu=theme_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand = 1)

theme_colors = {
    "dark": {
        "text_bg": "#343D46",
        "text_fg" : "#C6DEC1",
        "cursor" : "orange",
        "secelt_bg": "blue"
    },
    "light":{
        "text_bg": "#fff",
        "text_fg" : "#000",
        "cursor" : "#8000FF",
        "secelt_bg": "#777"
    }

}

text_o = Text(f_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'],
              padx=10, pady=10, font="Arial 12", wrap=WORD,
              insertbackground=theme_colors['dark']['cursor'],
              selectbackground=theme_colors['dark']['secelt_bg'], spacing3=10, width=10)
text_o.pack(fill=BOTH, expand = 1, side=LEFT)

scroll = Scrollbar(f_text, command=text_o.yview)
scroll.pack(fill=Y, side=LEFT )

text_o.config(yscrollcommand=scroll.set)

root.mainloop()