from functools import reduce

n = int(input("Кількість рядків та стовпців: "))


# Функція для обчислення елементів масиву А
def a_i(q, w):
    if (q + w) % 2 == 0:
        return sum([x for x in range(1, q + 1)])
    else:
        return sum([x ** 2 for x in range(1, w + 1)])

        # функція для обчислення елементів масиву b


def b_i(m, v):
    first_collomn = [m[b][v] for b in range(n)]
    return first_collomn


A = [[a_i(i, j) for j in range(1, n + 1)] for i in range(1, n + 1)]  # За допомогою функції формуєм матрицю
lis_of_dob = []
for g in range(n):
    dob_of_col = [reduce((lambda x, y: x * y), b_i(A, g))]  # Знаходимо добуток стовпця
    lis_of_dob += dob_of_col  # Додаємо добуток до масиву
print("Масив b: ", lis_of_dob)
list_of_par = [x for x in lis_of_dob if x % 2 == 0]  # Знаходимо список парних елементів
if len(list_of_par) > 0:  # Якщо він не пустий, то знаходимо найбільше
    print("Максимальне парне: ", max(list_of_par))
else:
    print("Нема ні одного парного числа")
