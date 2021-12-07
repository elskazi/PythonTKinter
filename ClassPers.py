class Person:
    name = "Vasia"

    def __init__(self, name):
        self.name = name
        self.nick = "Gogi"
        self.__age = 20

    def print_info(self):
        print(f'Привет меня зовут {self.name}, возраст {self.__age}, Ник {self.nick}')


    @property  # второй вариант вывода Геттера
    def ageeee(self):
        return self.__age

    @ageeee.setter # второй вариант вывода Cеттера
    def ageeee(self,value):
        if value in range(1, 101):  # сеттер в основном нужен для проверки
            self.__age = value
        else:
            print("EROOR WAWAWAW")