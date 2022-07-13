x1, y1, z1 = "Orange", "Banana", "Cherry"
print(x1, y1, z1)

x2 = y2 = z2 = "Orange"
print(id(x2), id(y2))
x2 = "Apple"
z2 = "Apple"
print(id(x2), id(y2), id(z2))

x, y, z = [x1, y1, z1]
print(x, y, z)