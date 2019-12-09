n = int(input("Кількість рядків: "))
m = int(input("Кількість стовпців:"))
A = [[float(input("A[{0}][{1}]= ".format(i, j))) for j in range(1, m + 1)]for i in range(1, n + 1)]
s = 0
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0 and A[i][j] < 0:
            s += A[i][j]
print("Сума від'ємних елементів: {0}".format(s))
