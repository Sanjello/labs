n = int(input("Кількість рядків та стовпців: "))
A = [[int(input("El[{0}][{1}]= ".format(i, j))) for j in range(1, n + 1)] for i in range(1, n + 1)]
matrix = [[0] * n for i in range(n)]
for j in range(n):
    for i in range(n):
        matrix[j][i] = A[i][j]
collumn = 0
for el in matrix:
    count = 0
    m = list(filter(lambda x: x < 0, el))
    if len(m) > 0:
        collumn += 1
        continue
    else:
        collumn += 1
        count = sum(el)
    print("Сума чисел стовпця № {0}: {1}".format(collumn, count))
