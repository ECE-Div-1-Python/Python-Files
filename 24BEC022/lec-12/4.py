# 4.	Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape. The class should also have a provision to accept the data relevant to the shape

class Shape:
    def __init__(self, side, sides):
        self.side = side
        self.sides = sides

    def perimeter(self):
        return self.side * self.sides

    def area(self):
        from math import tan, pi
        return (self.sides * self.side ** 2) / (4 * tan(pi / self.sides))

shape = Shape(5, 6)
print("Perimeter:", shape.perimeter())
print("Area:", shape.area())
