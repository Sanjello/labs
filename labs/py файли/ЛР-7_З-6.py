n = int(input("Кількість рядків та стовпців: "))
matrix = [[int(input("El[{0}][{1}]= ".format(i, j))) for j in range(1, n + 1)] for i in range(1, n + 1)]
matrix1 = [[0] * n for i in range(n)]
lis = []

for i in range(n):
    for j in range(n):
        matrix[i].reverse()
print(matrix)
