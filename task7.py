x1, y1 = input("Введіть координату х1, y1 поля(вводити х1 та у1 потрібно через кому(х1,у1)): ").split(",")
x2, y2 = input("Введіть координату х2, y2 поля(вводити х1 та у1 потрібно через кому(х1,у1)): ").split(",")
if 0 < int(x1) < 9 and 0 < int(x2) < 9 and 0 < int(y1) < 9 and 0 < int(y2) < 9:
    if abs(int(x1) - int(x2)) == abs(int(y1) - int(y2)) or int(x1) == int(x2) or int(y1) == int(y2):
        print("Ферзь за один хід може перейти з поля (х1;у1) на поле (х2;у2)")
    else:
        print("Ферзь за один хід не може перейти з поля ( х1;у1 ) на поле ( х2;у2 )")
else:
    print("Ферзь не може ходити за межі шахматного поля")
