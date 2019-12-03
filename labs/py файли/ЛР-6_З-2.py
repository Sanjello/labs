from math import sin, fabs, factorial
from functools import reduce


def a_i(m):
    return(((m - 1) ** 2) / 2 * (m ** 2) - 1) + factorial(m) * sin(m)


def dob(m):
    lis = []
    list_of_b = [reduce((lambda n, y: n * y), m, 1)]
    lis += list_of_b
    return lis


def count(m, e):
    lis = []
    list_of_b = [reduce((lambda n, y: fabs(n) + (a * fabs(y))), m, 1) for a in range(1, e + 1)]
    lis += list_of_b
    return lis


i = int(input("Кількість стовпців і рядків: "))
for v in range(1, i + 1):
    list_of_a = [a_i(v)]
    if a_i(i) < 0:
        lis = dob(list_of_a)
    else:
        lis = count(list_of_a, i)
print(lis)
