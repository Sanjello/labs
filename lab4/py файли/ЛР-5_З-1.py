from math import cos
a0 = 4
ai = 0
i = int(input("Введіть індекс числа: "))
while ai < i:
    if i == 0:
        break
    else:
        a0 = a0 - cos(a0/12)
        ai += 1
print(a0)
