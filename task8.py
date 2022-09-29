a = int(input("Введіть число A так, щоб A<B: "))
b = int(input("Введіть число B так, щоб A<B: "))
if a > b:
    print("Ви ввели неправильні числа.")
    quit()
else:
    for c in range(int(a), int(b) + 1):
        print(c)
if a == "1":
    print("Кількість чисел = " + str(b))
else:
    print("Кількість чисел = " + str(int(b) - int(a) + 1))
