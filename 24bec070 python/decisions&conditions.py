#2(a).1
a = 40
b = 30

x = (75 and a >= 20 and b < 60 and 35)

y = -30 and a >= 20 and b < 15 and 35

z = -30 and a >= 20 and 0 and 35

print("AND Results:")
print("x =", x)  
print("y =", y)  
print("z =", z)  

#2(a).2
a = 40
b = 30

x = 75 or a >= 20 and b < 60 and 35

x = 75 or a >= 20 or 60

y = a >= 20 or 75 or 60

z = a < 20 or 0 or 35

print("\nOR Results:")
print("x =", x)  
print("y =", y)  
print("z =", z)  

#2(a).3
a = 10
b = 20

result = not (a <= b)

print("\nNOT Result:")
print("result =", result) 




#2(b).1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest:", a)
    print("Smallest:", b)
else:
    print("Largest:", b)
    print("Smallest:", a)

#2(b).2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("Largest:", a)
elif b > c:
    print("Largest:", b)
else:
    print("Largest:", c)
if a < b and a < c:
    print("Smallest:", a)
elif b < c:
    print("Smallest:", b)
else:
    print("Smallest:", c)

#2(b).3
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#2(b).4
n = int(input("Enter a number: "))
if n % 10 == 0:
    print("Divisible by 10")
else:
    print("Not divisible by 10")

#2(b).5
age = int(input("Enter age: "))
if age < 18:
    print("Minor")
else:
    print("Major")

#2(b).6
n = int(input("Enter a number: "))
n = abs(n)
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10
print("Number of digits:", count)

#2(b).7
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#2(b).8
a1 = int(input("Enter angle 1: "))
a2 = int(input("Enter angle 2: "))
a3 = int(input("Enter angle 3: "))
if a1 + a2 + a3 == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

#2(b).9
n = int(input("Enter a number: "))
if n < 0:
    print("Absolute value:", -n)
else:
    print("Absolute value:", n)

#2(b).10
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
area = l * b
peri = 2 * (l + b)
if area > peri:
    print("Area is greater")
else:
    print("Perimeter is greater")

#2(b).11
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))
if (y2 - y1)*(x3 - x1) == (y3 - y1)*(x2 - x1):
    print("Points are collinear")
else:
    print("Points are not collinear")

#2(b).12
import math
x = int(input("Enter x: "))
y = int(input("Enter y: "))
cx = int(input("Enter center x: "))
cy = int(input("Enter center y: "))
r = int(input("Enter radius: "))
d = math.sqrt((x - cx)**2 + (y - cy)**2)
if d < r:
    print("Inside the circle")
elif d == r:
    print("On the circle")
else:
    print("Outside the circle")

#2(b).13
n = int(input("Enter number (0-19): "))
words = ["zero", "one", "two", "three", "four", "five", "six", "seven",
         "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
if 0 <= n <= 19:
    print(words[n])
else:
    print("Out of range")

#2(b).14
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
total = m1 + m2 + m3
avg = total / 3
print("Total:", total)
print("Average:", avg)
if m1 <= 39 or m2 <= 39 or m3 <= 39:
    print("Result: Fail")
else:
    print("Result: Pass")
for marks in [m1, m2, m3]:
    if marks == 0:
        print("Grade: NA")
    elif marks <= 39:
        print("Grade: F")
    elif marks <= 44:
        print("Grade: P")
    elif marks <= 49:
        print("Grade: C")
    elif marks <= 54:
        print("Grade: B")
    elif marks <= 59:
        print("Grade: B+")
    elif marks <= 69:
        print("Grade: A")
    elif marks <= 79:
        print("Grade: A+")
    elif marks <= 100:
        print("Grade: O")
