import math

class Solid:
    def __init__(self):
        self.shape = input("Enter shape (cube/cylinder): ").lower()
        if self.shape == "cube":
            self.side = float(input("Enter side length of cube: "))
        elif self.shape == "cylinder":
            self.radius = float(input("Enter radius of cylinder: "))
            self.height = float(input("Enter height of cylinder: "))
        else:
            print("Invalid shape")

    def surface_area(self):
        if self.shape == "cube":
            return 6 * self.side ** 2
        elif self.shape == "cylinder":
            return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        if self.shape == "cube":
            return self.side ** 3
        elif self.shape == "cylinder":
            return math.pi * self.radius ** 2 * self.height

s = Solid()
print("Surface Area:", s.surface_area())
print("Volume:", s.volume())
