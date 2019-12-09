n = int(input("Кількість рядків та стовпців: "))
matrix = [[int(input("Element[{0}][{1}]= ".format(i, j))) for j in range(1, n + 1)] for i in range(1, n + 1)]
vec = [int(input("Елемент вектора: ")) for i in range(n)]
for i in range(n):
    matrix[i] = list(map(lambda x, y: x * y, matrix[i], vec))
print(matrix)
