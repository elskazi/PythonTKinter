from tkinter import *


root = Tk()
root.title("Text & Scrollbar")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)

main_menu = Menu(root)
root.config(menu=main_menu)

def about_programm():
    print("Привет ")

def changt_theme(theme):
    text_o["bg"] = theme_colors[theme]["text_bg"],
    text_o["fg"] = theme_colors[theme]["text_fg"],
    text_o["insertbackground"] = theme_colors[theme]["cursor"],
    text_o["selectbackground"] = theme_colors[theme]["secelt_bg"],
    #print(theme)

#File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть")
file_menu.add_command(label="Сохранить")
file_menu.add_separator()
file_menu.add_command(label="Выход")
main_menu.add_cascade(label="Файл", menu=file_menu )

#theme
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0 )
theme_menu_sub.add_command(label="Белая", command = lambda : changt_theme('light'))
theme_menu_sub.add_command(label="Темная", command = lambda : changt_theme('dark'))
theme_menu.add_cascade(label="Тема", menu=theme_menu_sub)
theme_menu.add_command(label="О программе", command = about_programm)
main_menu.add_cascade(label="Разное", menu=theme_menu )

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



text_o = Text(f_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'], padx=10, pady=10, font="Arial 12", wrap=WORD,
              insertbackground=theme_colors['dark']['cursor'], selectbackground=theme_colors['dark']['secelt_bg'], spacing3=10, width=10 )
text_o.pack(fill=BOTH, expand = 1, side=LEFT)

scroll = Scrollbar(f_text, command=text_o.yview)
scroll.pack(fill=Y, side=LEFT )

text_o.config(yscrollcommand=scroll.set)

root.mainloop()