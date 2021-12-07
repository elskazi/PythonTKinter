'''Параметры со значениями по умолчанию у родительского класса, вариант 1'''

class Table:
    def __init__(self, l=1, w=1, h=1):
        self.length = l
        self.width = w
        self.height = h
        #print(self.length, self.width, self.height)


class KitchenTable(Table):
    places = 4

    def set_places(self, p):
        self.places = p
        return self.length* self.width* self.height* self.places
        #print(self.length, self.width, self.height, self.places)

#Table()

k = KitchenTable()
#k.places = 6
print(k.set_places() )