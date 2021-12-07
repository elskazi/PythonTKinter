class A:
    name = "Гость" # имя по умолчанию
    def say_hi(self, name=""): # имя пустое
        if name:
            return 'Hi ' + name
        else:
            return "Hello " + self.name  # Экземпляр объекта

a = A()
b = A()

print(a.say_hi())
print(b.say_hi("Petia"))
print(a.say_hi("Vasia"))
