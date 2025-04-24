class Shape:
    def __init__(self, x):
        self.x = x
    def area(self):
        return None
    def perimeter(self):
        return None
class Circle(Shape):

    def perimeter(self):
        return 2 * 3.14 * self.x['radius']
    def area(self):
        return 3.14 * (self.x['radius']) ** 2
class Square(Shape):
    def area(self):
        return (self.x['side']) ** 2
    def perimeter(self):
        return 2 * self.x['side']

Circle=Circle({'radius':5})
Square=Square({'side':5})
print("area of a Circle:",Circle.area())
print("perimeter of a Circle:",Circle.perimeter())
print("area of a Square:",Square.area())
print("perimeter of a Square:",Square.area())

