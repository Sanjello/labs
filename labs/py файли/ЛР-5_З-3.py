e = float(input("Введіть точність: "))
n = 1
x = float(input("Введіть число: "))
a = 1
b = 1
sum1 = 0
while sum1 > e:
    sum1 += (x ** n) / (a * b)

