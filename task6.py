x = input("Введіть координати (x) поля: ")
y = input("Введіть координати (у) поля: ")
c = int(y) % 2
if int(x) == 1 and c == 0:
    print("Поле біле")
elif int(x) == 1 and c == 1:
    print("Поле чорне")
else:
    if int(x) == 2 and c == 0:
        print("Поле чорне")
    elif int(x) == 2 and c == 1:
        print("Поле біле")
        quit()
c = int(y) % 2
if int(x) == 3 and c == 0:
    print("Поле біле")
elif int(x) == 3 and c == 1:
    print("Поле чорне")
else:
    if int(x) == 4 and c == 0:
        print("Поле чорне")
    elif int(x) == 4 and c == 1:
        print("Поле біле")
        quit()
if int(x) == 5 and c == 0:
    print("Поле біле")
elif int(x) == 5 and c == 1:
    print("Поле чорне")
else:
    if int(x) == 6 and c == 0:
        print("Поле чорне")
    elif int(x) == 6 and c == 1:
        print("Поле біле")
        quit()
if int(x) == 7 and c == 0:
    print("Поле біле")
elif int(x) == 7 and c == 1:
    print("Поле чорне")
else:
    if int(x) == 8 and c == 0:
        print("Поле чорне")
    elif int(x) == 8 and c == 1:
        print("Поле біле")