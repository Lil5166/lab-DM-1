x1, y1 = input("Введіть координати першої точки: ").split(";")
x2, y2 = input("Введіть координати другої точки: ").split(";")
a = int(x2) - int(x1)
b = int(y2) - int(y1)
s = a * b
p = (a + b) * 2
print("Периметр прямокутника = " + str(p))
print("Площа прямокутника = " + str(s))
