a = int(input("Введіть число а: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))
if a < b < c:
    print("Висловлення a<b<c правильне!")
else:
    print("Висловлення a<b<c не правильне!")
if a > 0 or b > 0 or c > 0:
    print("Хоча б одне з чисел додатнє")
else:
    print("Немає додатніх чисел")
if a > 0 and b < 0 and c < 0 or b > 0 and a < 0 and c < 0 or c > 0 and a < 0 and b < 0:
    print("Рівно одне з чисел додатнє")
