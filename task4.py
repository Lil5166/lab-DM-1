number = input("Введіть число, щоб перевірити його на парність: ")
a = int(number) % 2
if a == 0:
    print("Число парне")
else:
    print("Число не парне")