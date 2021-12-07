from tkinter import *

root = Tk()
root.title("Мое первое GUI приложение")
root.iconbitmap("ico.ico")
root.geometry("800x600+500+200")
root.resizable(TRUE,TRUE)

f = LabelFrame(root, text= "Калькулятор", padx=30, pady=20)
f.pack()

btn = [7,8,9,4,5,6,1,2,3,0]
row_m = 0
column_m = 0
# count_row = 0 # счетчик
# count_column = 0 # счетчик
for i in btn:
    if i==0:
        Button(f, text=i, width=4, height=2, ).grid(row=row_m, column=2)
    else:
        Button(f, text=i, width=4, height=2, ).grid(row=row_m, column=column_m)
        column_m+=1

        if column_m == 3:
            column_m =0
            row_m += 1


''' Если без перебора '''
# btn7 = Button(f, text="7",width=4, height=2,).grid(row=0, column=0),
# btn8 = Button(f, text="8",width=4, height=2,).grid(row=0, column=1),
# btn9 = Button(f, text="9",width=4, height=2,).grid(row=0, column=2),
#
# btn4 = Button(f, text="4",width=4, height=2,).grid(row=1, column=0),
# btn5 = Button(f, text="5",width=4, height=2,).grid(row=1, column=1),
# btn6 = Button(f, text="6",width=4, height=2,).grid(row=1, column=2),
#
# btn1 = Button(f, text="1",width=4, height=2,).grid(row=2, column=0),
# btn2 = Button(f, text="2",width=4, height=2,).grid(row=2, column=1),
# btn3 = Button(f, text="3",width=4, height=2,).grid(row=2, column=2),
#
# btn0 = Button(f, text="0",width=4, height=2,).grid(row=3, column=2),

root.mainloop()