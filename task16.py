a = input("Введіть перший рядок: ")
b = input("Введіть другий рядок: ")
print(a + b)
print(a * 10)
c = input("Що потрібно вставити? ")
d = int(input("Після якого символа (за номером) хочете вставити рядок?"))
print(a[:d] + c + a[d:], sep='')
