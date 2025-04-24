# 3.	Write a program to create a class that can calculate the surface area and volume of a solid. The class should also have a provision to accept the data relevant to the solid.


class Solid:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * 3.14 * self.radius * (self.radius + self.height)

    def volume(self):
        return 3.14 * self.radius ** 2 * self.height

solid = Solid(3, 5)
print("Surface Area:", solid.surface_area())
print("Volume:", solid.volume())

