from math import fabs
lis = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
a = int(input())
b = int(input())
lis2 = [x for x in lis if not (a <= fabs(x) <= b)]
lis3 = ([0] * (len(lis) - len(lis2)))
print(lis2 + lis3)
