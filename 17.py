'''Параметры со значениями по умолчанию у родительского класса, вариант 1'''
class Table:
    def __init__(self, l=1, w=1, h=1):
        self.length = l
        self.width = w
        self.height = h
        print(self.length, self.width, self.height)

class KitchenTable(Table):
    def __init__(self, l=1, w=1, h=1, p=1): # обязательно указывать начальные данные
        Table.__init__(self, l, w, h) #super().__init__(l,w, h) - можно через Супер
        self.p = p
    def print_info(self):
        print(self.length, self.width, self.height, self.p)

Table() # 1 1 1 принт убран
k = KitchenTable(100,100)
k.print_info() # 100 100 1 1
k2= KitchenTable(p=10)
k2.print_info() # 1 1 1 10
k3= KitchenTable(1,2,3,4)
k3.print_info() # 1 2 3 4