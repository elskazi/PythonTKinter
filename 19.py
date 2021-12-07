''' __str__ '''
class superClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printSuperClass(self):
        print(f"Name - {self.name}, age - {self.age} ")

    def __str__(self):
        return "Class " + self.__class__.__name__  #  Возвращение имени класса

class subClass(superClass):  # в скобках Основной Класс

    def __init__(self, name, age, company): # добавли новые данные(переменную)
        super().__init__(name,age) # взять из Основного класса класс __init__
        #superClass.__init__(self, name, age) #тут СЕЛФ обязательно
        self.company = company # созадем ствойства
    def pritnt_info(self):
        print(f"Name - {self.name}, age - {self.age}, company - {self.company} ") # записывается без селф
    def printSuperClass(self): # добали функцию
        super().printSuperClass() # взять из Основного класса класс printSuperClass # Name - Alan, age - 34
        print(f"company - {self.company} ")  # company - Google
    def __str__(self):
        #return f'Name: {self.name}'  # вариант 1 Возврашение какой то перменной
        return "Class " + self.__class__.__name__ # вариант 2 Возвращение имени класса

t1 = superClass("Alina", 33, )
print(t1) # Class superClass

t2=subClass("Alan", 34, "Google ")
#print(t2) # Name: Alan
print(t2) # Class subClass





