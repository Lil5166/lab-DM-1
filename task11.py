a = int(input("Введіть число: "))
k = 0
for i in range(2, a // 3):
    if a % i == 0:
        k = k + 1
if k <= 0:
    print("Число просте")
else:
    print("Число не є простим")
