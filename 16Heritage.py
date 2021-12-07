''' Дополняем подкласс новыми данными '''
class superClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printSuperClass(self):
        print(f"Name - {self.name}, age - {self.age} ")

class subClass(superClass):  # в скобках Основной Класс

    def subMy(self, company ="" ): # добавли новые данные(переменную)
           print(f"Name - {self.name}, age - {self.age}, company - {company} ") # записывается без селф

t1 = superClass("Alina", 33,) # передали данные в основной класс
t1.printSuperClass() # Name - Alina, age - 33

t2 = subClass("Alan", 34,) # передали данные в основной класс
t2.subMy("Google ") # Name - Alan, age - 34, company - Google  ... передали данные в подкласс


