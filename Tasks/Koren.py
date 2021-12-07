import math

print("ВВедите коэф для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

discr = b ** 2 - 4 * a * c
print("Дискриминант D =", discr)

if discr < 0:
    print(" Корня нет")
elif discr == 0:
    x1 = -b/(2*a)
    print(x1)
elif discr > 0:
    kDiscr = math.sqrt(discr) # возьмем корень
    x1 = (-b + kDiscr) / (2*a)
    x2 = (-b - kDiscr) / (2*a)
    print (x1, x2)