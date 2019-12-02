from math import sqrt
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
skalar_dob = x1 * x2 + y1 + y2
mod_a = sqrt(x1 ** 2 + x2 ** 2)
mod_b = sqrt(y1 ** 2 + y2 ** 2)
print(skalar_dob / (mod_a * mod_b))
