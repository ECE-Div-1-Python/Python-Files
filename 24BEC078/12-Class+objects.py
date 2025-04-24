#1.	Write a program to create a class that represents Complex numbers containing real and imaginary parts and then use it 
# to perform complex number addition, subtraction, multiplication and division.
class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imag=i
    def __add__(self,other):
        z=Complex(self,other)
        real=self.real + other.real
        imag=self.imag + other.imag
        return z
    def __sub__(self,other):
        z=Complex(self,other)
        real=self.real - other.real
        imag=self.imag - other.imag
        return z
    def __mul__(self,other):
        z=Complex(self,other)
        real=self.real*other.real-self.imag*other.imag
        imag=self.real*other.imag+self.imag*other.real
        return z
    def __truediv__(self,other):
        z=Complex(self, other)
        d=other.real**2 + other.imag**2
        if d==0:
            raise ZeroDivisionError("Division by zero error")
        real=(self.real*other.real + self.imag*other.imag)/d
        imag=(self.imag*other.real - self.real*other.imag)/d
    def __str__(self):
        return f"{self.real} + {self.imag}i"
c1 = Complex(4, 5)
c2 = Complex(2, -3)

print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)
"""*****************************************************************************************************************************"""
#2.	Write a program that implements a Matrix class and performs addition, multiplication and transpose 
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result_data = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result_data)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions for matrix multiplication.")
        result_data = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
             for j in range(other.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result_data)

    def transpose(self):
        transposed_data = [
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ]
        return Matrix(transposed_data)
    
matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8,10],[5,6,8]])

# Addition
sum_matrix = matrix1 + matrix2
print("Sum:\n", sum_matrix)

# Multiplication
product_matrix = matrix1 * matrix2
print("Multiplication:\n", product_matrix)

# Transpose
transpose_matrix = matrix1.transpose()
print("Transpose:\n", transpose_matrix)
"""*****************************************************************************************************************************"""
#3.	Write a program to create a class that can calculate the surface area and volume of a solid. The class should also have a provision to accept the data relevant to the solid.
class Solid:
    def __init__(self):
        self.shape=None
        self.dimensions={}
    def data(self):
        print("Choose solid type:")
        print("1.cube,2.cubiod,3.cylinder,4.sphere")
        a=int(input("Enter your choice(1-4):"))
        if a==1:
            self.shape="Cube"
            self.dimensions['side']=float(input("Enter a side of a cube:"))
        elif a==2:
             self.shape="cubiod"
             self.dimensions['length'] = float(input("Enter length: "))
             self.dimensions['breadth'] = float(input("Enter breadth: "))
             self.dimensions['height'] = float(input("Enter height: "))
        elif a==3:
            self.shape="cylinder"
            self.dimensions['radius'] = float(input("Enter radius: "))
            self.dimensions['height'] = float(input("Enter height: "))
        elif a == 4:
            self.shape="sphere"
            self.dimensions['radius'] = float(input("Enter radius: "))
        else:
            print("Invalid choice.")
            self.shape=None
    def surfacearea(self):
        if self.shape=="Cube":
            side=self.dimensions['side']
            return 6*(side**2)
        elif self.shape=="cubiod":
            l = self.dimensions['length']
            b = self.dimensions['breadth']
            h = self.dimensions['height']
            return 2 * (l*b + b*h + h*l)
        elif self.shape=="cylinder":
            r = self.dimensions['radius']
            return 4*(22/7)*r*r
        elif self.shape=="Sphere":
            r = self.dimensions['radius']
            return 4*(22/7)*r*r
        else:
            return None
    def volume(self):
        if self.shape=="Cube":
            side=self.dimensions['side']
            return side**3
        elif self.shape=="cubiod":
            l = self.dimensions['length']
            b = self.dimensions['breadth']
            h = self.dimensions['height']
            return l*b*h
        elif self.shape=="cylinder":
            r = self.dimensions['radius']
            h = self.dimensions['height']
            return (22/7)*r**2*h
        elif self.shape=="Sphere":
            r = self.dimensions['radius']
            return (4/3)*(22/7)*r**3
        else:
            return None
solid=Solid()
solid.data()
if solid.shape:
    print(f"solid type:{solid.shape}")
    print(f"Surface area:{solid.surfacearea():.2f}")
    print(f"Volume: {solid.volume():.2f}")
"""*****************************************************************************************************************************"""        
#4.	Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape. The class should also have a provision to accept the data relevant to the shape.
import math
class RegularShape:
    def __init__(self):
        self.shape_type = None
        self.parameters = {}

    def accept_data(self):
        print("Choose a shape:")
        print("1. Square")
        print("2. Circle")
        print("3. Equilateral Triangle")
        print("4. Regular Polygon")
        choice = int(input("Enter choice (1-4): "))
        
        if choice == 1:
            self.shape_type = "Square"
            side = float(input("Enter side length: "))
            self.parameters['side'] = side

        elif choice == 2:
            self.shape_type = "Circle"
            radius = float(input("Enter radius: "))
            self.parameters['radius'] = radius

        elif choice == 3:
            self.shape_type = "Equilateral Triangle"
            side = float(input("Enter side length: "))
            self.parameters['side'] = side

        elif choice == 4:
            self.shape_type = "Regular Polygon"
            n = int(input("Enter number of sides: "))
            side = float(input("Enter length of one side: "))
            self.parameters['n'] = n
            self.parameters['side'] = side

        else:
            print("Invalid choice.")

    def calculate_perimeter(self):
        if self.shape_type == "Square":
            return 4 * self.parameters['side']

        elif self.shape_type == "Circle":
            return 2 * math.pi * self.parameters['radius']

        elif self.shape_type == "Equilateral Triangle":
            return 3 * self.parameters['side']

        elif self.shape_type == "Regular Polygon":
            return self.parameters['n'] * self.parameters['side']

        else:
            return None

    def calculate_area(self):
        if self.shape_type == "Square":
            return self.parameters['side'] ** 2

        elif self.shape_type == "Circle":
            return math.pi * (self.parameters['radius'] ** 2)

        elif self.shape_type == "Equilateral Triangle":
            side = self.parameters['side']
            return (math.sqrt(3) / 4) * side ** 2

        elif self.shape_type == "Regular Polygon":
            n = self.parameters['n']
            s = self.parameters['side']
            # Using formula: (n * s^2) / (4 * tan(π/n))
            return (n * s ** 2) / (4 * math.tan(math.pi / n))

        else:
            return None

shape = RegularShape()
shape.accept_data()

perimeter = shape.calculate_perimeter()
area = shape.calculate_area()

if perimeter is not None and area is not None:
    print(f"\nShape: {shape.shape_type}")
    print(f"Perimeter/Circumference: {perimeter:.2f}")
    print(f"Area: {area:.2f}")
else:
    print("Could not calculate. Please enter valid shape data.")


"""*****************************************************************************************************************************""" 
#5.	Write a program that creates and uses a Time class to perform various time arithmetic operations.
class Time:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
        self._normalize()
    def _normalize(self):
        self.m+=self.s//60
        self.s%=60
        self.h+=self.m//60
        self.m%=60
    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"
    def __add__(self,other):
        return Time(self.h+other.h,self.m+other.m,self.s+other.s)
    def __sub__(self,other):
        diff=abs(self.to_sec()-other.to_sec())
        return Time.from_sec(diff)
    def to_sec(self):
        return self.h*3600 + self.m*60 + self.s
    def to_min(self):
        return self.h*60+self.m +self.s/60
    @staticmethod
    def from_sec(sec):
        h,sec=divmod(sec,3600)
        m,s=divmod(sec,60)
        return Time(h,m,s)
t1 = Time(2, 45, 50)
t2 = Time(1, 20, 15)
print(t1,t2)
print("sum:",t1+t2)
print("Difference:", t1 - t2)
print("Time 1 in seconds:", t1.to_sec())
print("Time 1 in minutes:", t1.to_min())

#6.	Write a program to create a class Date that has a list containing day, month and year attributes. Define an overloaded == operator to compare two Date objects.
class Date:
    def __init__(self,d,m,y):
        self.date=[d,m,y]
    def __eq__(self,other):
        return self.date==other.date
    def __str__(self):
        return f"{self.date[0]:02}-{self.date[1]:02}-{self.date[2]:02}"
d1=Date(4,5,2025)
d2=Date(4,5,2024)
d3=Date(4,5,2025)
print("Date1:",d1)
print("Date2:",d2)
print(d1==d2)
print(d1==d3)

#7.	Create a class Weather that has a list containing weather parameters.
#  Define an overloaded in operator that checks whether an item is present in the list.
#  (Hint: define the function __contains__( )in a class.)

class Weather:
    def __init__(self, *params): 
        self.data = list(params)
    def __contains__(self, item): 
        return item in self.data
    def __str__(self): 
        return f"Weather Data: {', '.join(self.data)}"

w = Weather("Rain", "Sunny", "Cloudy", "Windy")
print(w)
print("Rain" in w)
print("Snow" in w)

class String:
    def __init__(self, value): self.text = value
    def __iadd__(self, other): self.text += other.text; return self
    def toLower(self): self.text = self.text.lower()
    def toUpper(self): self.text = self.text.upper()
    def __str__(self): return self.text

#	Implement a String class containing the following functions:
#a.	Overloaded += operator function to perform string concatenation
#b.	Method toLower() to convert upper case letters to lower case.
#c.	Method toUpper() to convert lower case letters to upper case.
s1 = String("Hello")
s2 = String(" World")
s1 += s2
print("Concatenated:", s1)

s1.toLower()
print("Lowercase:", s1)

s1.toUpper()
print("Uppercase:", s1)
