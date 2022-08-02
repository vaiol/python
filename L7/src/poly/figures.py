# ovveride method
# abstract class, abstract methods
# polymorphism

from abc import ABC, abstractclassmethod
import math
from turtle import circle

class Figure:
    def __init__(self):
        pass

    @abstractclassmethod
    def perimeter(self):
        pass

    @abstractclassmethod
    def area(self):
        pass

    def __str__(self):
        return 'This is Figure'

    def combined(self):
        return self.area() + self.perimeter()



# Круг
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius


    def perimeter(self):
        return (2 * math.pi * self.radius)

    def area(self):
        return (math.pi * self.radius * self.radius)

    def combined(self, v1):
        return self.area() + self.perimeter() + v1
    
    def combined_v2(self, v1, v2):
        return self.area() + self.perimeter() + v1 + v2






# c = Circle(5)
# c10 = Circle(10)


# Квадрат
class Square(Figure):
    def __init__(self, edge):
        self.edge = edge


    def perimeter(self):
        return self.edge * 4


    def area(self):
        return self.edge * self.edge


    def __str__(self):
        return f'Square, area={self.area()}, perimeter={self.perimeter()}'

# Прямотник
class Rectangle(Figure):
    def __init__(self, a, b):
        self.edge_a = a
        self.edge_b = b


    def perimeter(self):
        return self.edge_a * 2 + self.edge_b * 2


    def area(self):
        return self.edge_a * self.edge_b


    def __str__(self):
        return f'Rectangle, area={self.area()}, perimeter={self.perimeter()}'


rec = Rectangle(5, 12)
rec_2 = Rectangle(6, 18)
circ = Circle(5)
sqr = Square(5)

print(circ.combined(1))
print(circ.combined_v2(1, 2))


print(isinstance(rec, Figure))
print(isinstance(rec_2, Figure))
print(isinstance(circ, Figure))
print(isinstance(sqr, Figure))

mixed_arr: list[Figure] = ['123', rec, rec_2, circ, sqr, 1, {}]
for item in mixed_arr:
    if isinstance(item, Figure):
        print('This is figure, and area is', item.area())
    else:
        print('This is not a figure', item)













# print(issubclass(Rectangle, Figure)) # True
# print(isinstance(rec, Rectangle)) # True
# print(isinstance(rec, Figure)) # True

# arr = [rec, circ, sqr]
# for item in arr:
#     print(item)
# print()
# # sort by area
# arr.sort(key=lambda item: item.area())
# for item in arr:
#     print(item)
# print()
# # sort by perimeter
# arr.sort(key=lambda item: item.perimeter())
# for item in arr:
#     print(item)