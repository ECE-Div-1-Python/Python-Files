#q1)
def Ls3():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    if(a>b):
        print("Smallest value:", b, "Largest value:", a)
    else:
        print("Smallest value:", a, "Largest value:", b)
Ls3()

#q2)
def Ls3():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    if(a>b) and (a>c):
        print("The largest value is ", a)
    elif(b>c):
        print("The largest value is ", b)
    elif(c>b):
        print("The largest value is", c)
    else:
        print("All numbers are equal")
Ls3()

#q3)
def Num1():
    n1 = int(input("Enter the value of n1: "))
    if(n1%2 == 0):
        print("Even number is n1 = ", n1)
    else:
        print("Odd number is n1 = ", n1)
Num1()

#q4)
def A1():
    n1 = int(input("Enter the value of n1: "))
    if(n1%10 == 0):
        print("n1 is Divisible by 10")
    else:
        print("n1 is not Divisible by 10")
A1()

#q5)
def Ag():
    Age = int(input("The age of a person is:"))
    if(Age < 18):
        print("Minor")
    else:
        print("Major")
Ag()

#q6)
def N2():
    n1 = int(input("Enter the value of n1: "))
    n2 = str(n1)
    n3 = len(n2)
    print("The number of digits in a number :", n3)
N2()

#q7)
def Y1():
    Year = int(input("The Year is:"))
    if(Year%4 == 0):
        print("Leap year")
    else:
        print("Not Leap year")
Y1()

#q8)
def An1():
    a1 = int(input("Enter the value of angle 1: "))
    a2 = int(input("Enter the value of angle 2: "))
    a3 = int(input("Enter the value of angle 3: "))
    if(a1+a2+a3 == 180):
        print("Valid triangle")
    else:
        print("Not valid")
An1()

#q9)
def Ab1():
    a = int(input("Enter the value of a: "))
    if number < 0:
        absolute_value = -number
    else:
        absolute_value = number
        print("Absolute value:", absolute_value)
Ab1()


#q10)
def L1():
    l = int(input("Enter the value of l: "))
    w = int(input("Enter the value of w: "))
    area = l*w
    perimeter = 2(l+w)
    if(area > perimeter):
        print("Area of rectangle is greater")
    else:
        print("Perimeter is greater")
L1()

#q11)
def C1():
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        print("The points are collinear.")
    else:
        print("The points are not collinear.")
C1()

#q12)
import math
x = float(input("Enter x-coordinate of circle center: "))
y = float(input("Enter y-coordinate of circle center: "))
r = float(input("Enter radius of the circle: "))
px = float(input("Enter x-coordinate of the point: "))
py = float(input("Enter y-coordinate of the point: "))

distance = math.sqrt(pow(px - x, 2) + pow(py - y, 2))

if distance < r:
    print("The point lies inside the circle.")
elif distance == r:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")

