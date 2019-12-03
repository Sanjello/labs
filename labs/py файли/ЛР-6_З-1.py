from functools import reduce
from math import inf
num = int(input("Кількість чисел:"))
list_of_num = [int(input())for i in range(num)]
maxnum = reduce((lambda maxN, el: el if maxN < el < 0 else maxN), list_of_num, - inf)
print(maxnum)
