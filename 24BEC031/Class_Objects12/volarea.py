import math
class Solid:
    def __init__(self, shape_type, *dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

        if shape_type == "sphere":
            if len(dimensions) != 1:
                raise ValueError("Sphere requires 1 dimension: radius")
            self.radius = dimensions[0]
        elif shape_type == "cylinder":
            if len(dimensions) != 2:
                raise ValueError("Cylinder requires 2 dimensions: radius and height")
            self.radius, self.height = dimensions
        elif shape_type == "cuboid":
            if len(dimensions) != 3:
                raise ValueError("Cuboid requires 3 dimensions: length, width, and height")
            self.length, self.width, self.height = dimensions
        else:
            raise ValueError("Unsupported shape type")

    def surface_area(self):
        if self.shape_type == "sphere":
            return 4 * math.pi * self.radius ** 2
        elif self.shape_type == "cylinder":
            return 2 * math.pi * self.radius * (self.radius + self.height)
        elif self.shape_type == "cuboid":
            return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def volume(self):
        if self.shape_type == "sphere":
            return (4 / 3) * math.pi * self.radius ** 3
        elif self.shape_type == "cylinder":
            return math.pi * self.radius ** 2 * self.height
        elif self.shape_type == "cuboid":
            return self.length * self.width * self.height

    def disp(self):
        print(f"Shape: {self.shape_type.capitalize()}")
        print(f"Surface Area: {self.surface_area():.2f}")
        print(f"Volume: {self.volume():.2f}")


if __name__ == "__main__":
    sphere = Solid("sphere", 5)
    sphere.disp()

    cylinder = Solid("cylinder", 3, 7)
    cylinder.disp()

    cuboid = Solid("cuboid", 4, 6, 8)
    cuboid.disp()
