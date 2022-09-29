a = int(input("Введіть розмір масиву: "))
b = 0
c = [0] * a
for i in range(a):
    print("Введіть " + str(i + 1) + "-й елемент масиву")
    c[i] = int(input())
    b += c[i]
d = b / a
for i in range(a):
    if c[i] > d:
        c[i] -= 18
print(c)
