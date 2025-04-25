import math
class RegularShape:
    def __init__(self, shape_type, *dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions

        if self.shape_type == "circle":
            if len(dimensions) != 1:
                raise ValueError("Circle requires 1 dimension: radius")
            self.radius = dimensions[0]
        elif self.shape_type == "square":
            if len(dimensions) != 1:
                raise ValueError("Square requires 1 dimension: side length")
            self.side = dimensions[0]
        elif self.shape_type == "rectangle":
            if len(dimensions) != 2:
                raise ValueError("Rectangle requires 2 dimensions: length and width")
            self.length, self.width = dimensions
        elif self.shape_type == "triangle":
            if len(dimensions) != 1:
                raise ValueError("Equilateral Triangle requires 1 dimension: side length")
            self.side = dimensions[0]
        else:
            raise ValueError("Bad shape type. Supported shapes: circle, square, rectangle, triangle")

    def perimeter_or_circumference(self):
        """Calculate perimeter or circumference based on shape type."""
        if self.shape_type == "circle":
            return 2 * math.pi * self.radius
        elif self.shape_type == "square":
            return 4 * self.side
        elif self.shape_type == "rectangle":
            return 2 * (self.length + self.width)
        elif self.shape_type == "triangle":
            return 3 * self.side

    def area(self):
        """Calculate area based on shape type."""
        if self.shape_type == "circle":
            return math.pi * self.radius ** 2
        elif self.shape_type == "square":
            return self.side ** 2
        elif self.shape_type == "rectangle":
            return self.length * self.width
        elif self.shape_type == "triangle":
            return (math.sqrt(3) / 4) * self.side ** 2

    def disp(self):
        print(f"Shape: {self.shape_type.capitalize()}")
        print(f"Perimeter/Circumference: {self.perimeter_or_circumference():.2f}")
        print(f"Area: {self.area():.2f}")


# Example usage
if __name__ == "__main__":
    circle = RegularShape("circle", 5)
    circle.disp()

    square = RegularShape("square", 4)
    square.disp()

    rectangle = RegularShape("rectangle", 4, 6)
    rectangle.disp()

    triangle = RegularShape("triangle", 5)
    triangle.disp()
