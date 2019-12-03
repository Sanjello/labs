x = int(input("x: "))
y = int(input("y: "))
e = int(input("e: "))
if y < x:
    z = y * (e ** x)
elif y > x:
    z = x * (e ** y)
else:
    z = y * x
print("Z = ", z)
