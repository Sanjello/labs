num = int(input("Кількість чисел:"))
list_of_num = [int(input("Число:")) for i in range(num)]
print("max negative: {0}".format(max([x for x in list_of_num if x < 0])))
