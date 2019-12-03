n = int(input())
z = 0
while n > 0:
    m = n % 10
    if m > z:
        z = m
    n = n // 10
print(z)
