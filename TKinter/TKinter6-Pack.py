from tkinter import *

root = Tk()
root.title("Мое первое GUI приложение")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)

''' Frame без границы, без рамки '''
# f_top = Frame(root)
# f_bottom = Frame(root)
# f_top.pack()
# f_bottom.pack()

''' LabelFrame бс границей, с рамкой '''
f_top = LabelFrame(root, text= "TOP Frame", padx=30, pady=20) # внутренние отступыы
f_bottom = LabelFrame(root, text= "BOTTOM Frame", padx=30, pady=20)
f_top.pack(pady=20) # внешнии отступы
f_bottom.pack()

l1 = Button(f_top, text="1",  bg="#ff0000", width=8, height= 4,).pack(side="left")
l2 = Button(f_top, text="2",  bg="#ff7d00", width=8, height= 4,).pack(side="left")
l3 = Button(f_bottom, text="3",  bg="#ffff00", width=8, height= 4,).pack(side="left")
l4 = Button(f_bottom, text="4",  bg="#00ff00", width=8, height= 4,).pack(side="left")

l5 = Button(root, text="1",  bg="#ff0000", width=8, height= 4,).pack(expand=1, fill=BOTH, anchor=SW)
# expand - выравнирвание по середине ,
# fill - заполнение X Y BOTH
# side -  выравнивание верх право низ лево
# anchor - выравнивание по сторонам света, только вметсе с expand

root.mainloop()