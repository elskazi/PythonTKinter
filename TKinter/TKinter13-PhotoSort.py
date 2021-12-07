from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import os
from datetime import datetime

root = Tk()
root.title("Фото Сортировка")
#root.iconbitmap("C:\\PythonTrinter\\TKinter\\notepad\\ico.ico")
root.geometry("500x300+300+200")
root.resizable(TRUE,TRUE)

s = ttk.Style()
s.configure('my.TButton', font=("Helvetica", 15))

def choose_dir():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, dir_path)


def f_start():
    cur_path = e_path.get()
    if cur_path:
        for folder, subfolders, files in os.walk(cur_path):
            # print(files) # покажет все файлы в папке
            for file in files:
                path=os.path.join(folder, file)
                #print(path) # покажет пути и файлы
                mtime = os.path.getmtime(path)
                #print(mtime) # покажет время прошедшее с модификации файла, в дибильном формате
                date = datetime.fromtimestamp(mtime) # в человеческую дату переводим
                #print(date)
                date = date.strftime("%Y-%m-%d") # YYYY-MM-DD меняем формат
                #print(date)
                date_folder = os.path.join(cur_path, date) # соединяем папку и дату
                #print(date_folder)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo("Готово", "Сортировка выполнена успешно")
        e_path.delete(0, END)

    else:
        messagebox.showwarning("Внимание", "Выберите папку с фото")




frame = Frame(root, bg="#56AdFF", bd=5)
frame.pack(pady=10, padx=10, fill=X)

e_path = ttk.Entry(frame,)
e_path.pack(side=LEFT, ipady=4,pady=2, expand=True, fill=X)

btn_dialog = ttk.Button(frame, text="Выбрать папку", command=choose_dir)
btn_dialog.pack(side=LEFT, padx=20)

btn_start = ttk.Button(root, text="Старт", style="my.TButton" ,command=f_start)
btn_start.pack( padx=5, ipady=4, ipadx=4)

root.mainloop()