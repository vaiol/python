# ovveride method
# abstract class, abstract methods
# polymorphism

from abc import ABC, abstractclassmethod
import math
from turtle import circle

class Figure(ABC):
    @abstractclassmethod
    def perimeter(self):
        pass
    @abstractclassmethod
    def area(self):
        pass
    @abstractclassmethod
    def __str__(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return (2 * math.pi * self.radius)
    def area(self):
        return (math.pi * self.radius * self.radius)
    def __str__(self):
        return f'Circle, area={self.area()}, perimeter={self.perimeter()}'

class Square(Figure):
    def __init__(self, edge):
        self.edge = edge
    def perimeter(self):
        return self.edge * 4
    def area(self):
        return self.edge * self.edge
    def __str__(self):
        return f'Square, area={self.area()}, perimeter={self.perimeter()}'

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


# f = Figure() # помилка абстрактний класс
rec = Rectangle(5, 12)
circ = Circle(5)
sqr = Square(5)


print(issubclass(Rectangle, Figure)) # True
print(isinstance(rec, Rectangle)) # True
print(isinstance(rec, Figure)) # True

arr = [rec, circ, sqr]
for item in arr:
    print(item)
print()
# sort by area
arr.sort(key=lambda item: item.area())
for item in arr:
    print(item)
print()
# sort by perimeter
arr.sort(key=lambda item: item.perimeter())
for item in arr:
    print(item)