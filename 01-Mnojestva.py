'''print( "Таблица умножения")

for i in range(1,10):
    for k in range(1,10):
        print(f'{i} * {k} = {i * k}\t', end=' ')
    print(' ')
else:
    print(" end ")'''

def tab(x,y,a,b):
    for i in range(x, y):
        for k in range(a, b):
            print(f'{i} * {k} = {i * k}\t', end=' ')
        print(' ')
    else:
        print(" end ")

tab(1,11,1,3)
