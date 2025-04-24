1)

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

a = Complex(4, 5)
b = Complex(2, 3)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

2)

class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __add__(self, other):
        result = [[self.mat[i][j] + other.mat[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __mul__(self, other):
        result = [[sum(self.mat[i][k] * other.mat[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        return Matrix(result)

    def transpose(self):
        result = [[self.mat[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def display(self):
        for row in self.mat:
            print(row)

A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Addition:")
(A + B).display()
print("Multiplication:")
(A * B).display()
print("Transpose of A:")
A.transpose().display()

3)

class Solid:
    def __init__(self, shape, **kwargs):
        self.shape = shape
        self.params = kwargs

    def surface_area(self):
        if self.shape == "cube":
            a = self.params["side"]
            return 6 * a * a
        elif self.shape == "sphere":
            r = self.params["radius"]
            return 4 * 3.1416 * r * r

    def volume(self):
        if self.shape == "cube":
            a = self.params["side"]
            return a ** 3
        elif self.shape == "sphere":
            r = self.params["radius"]
            return (4/3) * 3.1416 * r ** 3

cube = Solid("cube", side=5)
print("Cube Surface Area:", cube.surface_area())
print("Cube Volume:", cube.volume())

4)

class Shape:
    def __init__(self, shape, **kwargs):
        self.shape = shape
        self.params = kwargs

    def area(self):
        if self.shape == "circle":
            r = self.params["radius"]
            return 3.1416 * r * r
        elif self.shape == "square":
            a = self.params["side"]
            return a * a

    def perimeter(self):
        if self.shape == "circle":
            r = self.params["radius"]
            return 2 * 3.1416 * r
        elif self.shape == "square":
            a = self.params["side"]
            return 4 * a

circle = Shape("circle", radius=7)
print("Circle Area:", circle.area())
print("Circle Circumference:", circle.perimeter())

5)

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_time(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        total_minutes %= 60
        return Time(total_hours, total_minutes)

    def display(self):
        print(f"{self.hours}h {self.minutes}m")


t1 = Time(2, 45)
t2 = Time(1, 30)
result = t1.add_time(t2)
result.display()

6)

class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        return self.date == other.date

d1 = Date(24, 4, 2025)
d2 = Date(24, 4, 2025)
print("Dates are equal:", d1 == d2)

7)

class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

w = Weather(["rainy", "cloudy", "sunny"])
print("rainy" in w)
print("snowy" in w)

8)

class MyString:
    def __init__(self, string=""):
        self.string = string

    def __iadd__(self, other):
        self.string += other.string
        return self

    def toLower(self):
        return self.string.lower()

    def toUpper(self):
        return self.string.upper()

s1 = MyString("Hello")
s2 = MyString("World")
s1 += s2
print("Concatenated:", s1.string)
print("Lowercase:", s1.toLower())
print("Uppercase:", s1.toUpper())



