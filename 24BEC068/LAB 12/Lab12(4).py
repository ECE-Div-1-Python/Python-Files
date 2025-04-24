import math

class Shape:
    def __init__(self):
        self.shape = input("Enter shape (square/rectangle/circle): ").lower()
        if self.shape == "square":
            self.side = float(input("Enter side of square: "))
        elif self.shape == "rectangle":
            self.length = float(input("Enter length: "))
            self.breadth = float(input("Enter breadth: "))
        elif self.shape == "circle":
            self.radius = float(input("Enter radius: "))
        else:
            print("Invalid shape")

    def area(self):
        if self.shape == "square":
            return self.side ** 2
        elif self.shape == "rectangle":
            return self.length * self.breadth
        elif self.shape == "circle":
            return math.pi * self.radius ** 2

    def perimeter(self):
        if self.shape == "square":
            return 4 * self.side
        elif self.shape == "rectangle":
            return 2 * (self.length + self.breadth)
        elif self.shape == "circle":
            return 2 * math.pi * self.radius

s = Shape()
print("Area:", s.area())
print("Perimeter/Circumference:", s.perimeter())
