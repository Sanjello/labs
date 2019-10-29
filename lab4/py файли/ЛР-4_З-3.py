import math as m
x1 = float(input("x1: "))
y1 = float(input("y1: "))
y2 = float(input("y2: "))
x2 = float(input("x2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))
AB = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
BC = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
AC = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
e = 0.0001
if m.abs(AB-AC) < e or m.abs(BC-AC) < e or m.abs(AB-AC) < e:
    print("Трикутник рівнобедренний(З точнітю до 3-х знаків)")
else:
    print("Трикутник не рівнобедренний")
