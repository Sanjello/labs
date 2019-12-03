from math import sqrt
vek_a = [int(input())for i in range(2)]
vek_b = [int(input())for s in range(2)]
skalar_dob = vek_a[0] * vek_b[0] + vek_a[1] * vek_b[1]
mod_a = sqrt(vek_a[0] ** 2 + vek_b[0])
mod_b = sqrt(vek_a[1] ** 2 + vek_b[1])
print("cos = ", skalar_dob / (mod_a * mod_b))
