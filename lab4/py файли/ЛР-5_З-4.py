i = int(input('Введіть номер(>= 3):'))
x0 = 0
x1 = 9
x2 = 9
n = 3
while n <= i:
    xi = x2 + x1 + x0
    x0 = x1
    x1 = x2
    x2 = xi
    n += 1
print(x2)
