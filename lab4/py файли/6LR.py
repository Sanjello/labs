n = int(input("Кількість чисел:"))
list1 = [float(input())for i in range(n)]
list2 = [x for x in list1 if x < 0]
max1 = max(list2)
print("Максимальне від'ємне:", max1)