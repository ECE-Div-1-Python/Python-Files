#1) Print largest and smallest values out of two.
def ls2():

 a=int(input("Enter first number:"))
 b=int(input("Enter second number:"))
 if a>b:
    print(a,"is largest number")
    print(b,"is smallest number")
 else:
    print(b,"is lagest number")
    print(a,"is smallest number")
ls2()

"""---------------------------------------------------------------------------------------------------------------------------------"""
#2) Print largest and smallest values out of three.
def ls3():  
 a=int(input("Enter first number:"))
 b=int(input("Enter second number:"))
 c=int(input("Enter third number:"))
 if a>b and a>c:
    print(a,"is largest number")
 elif b>c and b>a:
   print(b,"is largest number")
 else:
   print(c,"is lagest number")
ls3()

"""---------------------------------------------------------------------------------------------------------------------------------"""
#3) Check whether a given number is odd or even.
def oddeven():
    a=int(input("Enter a number"))
    if a%2==0:
        print(a," is even number")
    else:
        print(a,"is odd number")
oddeven()    

"""---------------------------------------------------------------------------------------------------------------------------------"""
#4) Check whether a given number is divisible by 10 or not.
def divisible():
    a=int(input("Enter a number"))
    if a%10==0:
        print(a,"is divisible by 10")
    else:
         print(a,"is not divisible by 10")
divisible()        

"""---------------------------------------------------------------------------------------------------------------------------------"""
#5) Accept age of a person. If age is less than 18, print minor otherwise Major.
def agecal():
    age=int(input("Enter the age of a person:"))
    if age<18:
        print("Minor")
    else:
        print("Major")
agecal() 

"""---------------------------------------------------------------------------------------------------------------------------------"""
#6) Accept a number from the user. And print number of digits in it.
def countdigit():
    a=int(input("Enter a number:"))
    if a<10:
        Print("The number is in one digit")
    elif a<100 and a>10:
        print("The number is in two digits")
    elif a>100 and a <1000:
        print("The number is in three digits")
    else:
        print("Thhe number is more than three digits")
countdigit()

"""---------------------------------------------------------------------------------------------------------------------------------"""
#7) Accept a year value from the user. Check whether it is a leap year or not
def leapyear():
    year=int(input("Enter a year:"))
    if year%400==0 and year%100==0:
        print(f'{year} is a leap year.')
    elif year%4==0 and year%100!=0:
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')
leapyear()        
     
"""---------------------------------------------------------------------------------------------------------------------------------"""
"""8) Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard.
A triangle is valid if the sum of all the three angles is equal to 180 degree"""
def triangle():
 angle1=float(input("Enter angle no.1:"))
 angle2=float(input("Enter angle no.2:"))
 angle3=float(input("Enter angle no.3:"))
 if angle1>0 and angle2>0 and angle3>0 and (angle1+angle2+angle3)==180:
     print("The triangle is valid.")
 else:
     print("The triangle is  not valid.") 
triangle()
 
"""---------------------------------------------------------------------------------------------------------------------------------"""
#9) Print absolute value of a given number
def absoluteno():
    number=float(input("Enter a number"))
    if number<0:
      absolutevalue=-number
    else:
      absolutevalue=number
    print(f"The absolute value of {number} is {absolutevalue}")  
absoluteno()      
      
"""---------------------------------------------------------------------------------------------------------------------------------"""
#10) Given the length and breadth of a rectangle, write a program to find whether the are of the rectangle is greater than its perimeter.
def rectangle():
    l=int(input("Enter a length of the rectangle:"))
    b=int(input("Enter a breadth of the rectangle:"))
    area=l*b
    perimeter=2*(l+b)
    if area>perimeter :
        print("area of the rectangle is greater than its perimeter.")
    else:
        print("area of the rectangle is not greater than its perimeter.")
rectangle()        

"""---------------------------------------------------------------------------------------------------------------------------------"""
#11) Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straightline
def point_in_straight_line():
    x1=float(input("Enter x1 point"))
    y1=float(input("Enter y1 point"))
    x2=float(input("Enter x2 point"))
    y2=float(input("Enter y2 point"))
    x3=float(input("Enter x3 point"))
    y3=float(input("Enter y3 point"))
    m= (y2-y1)/(x2-x1)
    n= (y3-y2)/(x3-x2)
    if m==n:
        print("all the points are fall on one straight line.")
    else:
        print("all the points are  not fall on one straight line.")
point_in_straight_line()

"""---------------------------------------------------------------------------------------------------------------------------------"""
# Given the coordinates (x,y) of center of a circle and its radius, determine whether a point liesinside the circle, on the circle or outside the circle.
def pointoncircle():
    circle_x=int(input("Enter x:"))
    circle_y=int(input("Enter y:"))
    pointx=int(input("Enter point x:"))
    pointy=int(input("Enter point y:"))
    radius=int(input("Enter radius:"))
    radius_square= radius**2
    distance_square= (circle_x-pointx)**2 + (circle_y-pointy)**2
    if radius_square>distance_square :
        print("points are inside the circle")
    elif  radius_square==distance_square :   
        print("points are on the the circle")
    else:
        print("points are outside the circle")
pointoncircle()

"""---------------------------------------------------------------------------------------------------------------------------------"""
# Given the coordinates (x,y) of center of a circle and its radius, determine whether a point liesinside the circle, on the circle or outside the circle.
def pointoncircle():
    circle_x=int(input("Enter x:"))
    circle_y=int(input("Enter y:"))
    pointx=int(input("Enter point x:"))
    pointy=int(input("Enter point y:"))
    radius=int(input("Enter radius:"))
    radius_square= radius**2
    distance_square= (circle_x-pointx)**2 + (circle_y-pointy)**2
    if radius_square>distance_square :
        print("points are inside the circle")
    elif  radius_square==distance_square :   
        print("points are on the the circle")
    else:
        print("points are outside the circle")
pointoncircle()

"""---------------------------------------------------------------------------------------------------------------------------------"""
#13) Convert number 0 to 19 to its equivalent words. E.g. 0 → zero, 19→nineteen.
def numberofwords():
    words = ["zero","one","two","three","four","five","six","seven","eight","nine","ten",
             "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    n=int(input("Enter number:"))
    if 0<=n<=19:
        return words[n]
    else:
        return "Number is not in range"
print(numberofwords())

"""---------------------------------------------------------------------------------------------------------------------------------"""
"""14) Accept marks of three subjects. Print total and average along with whether a candidate haspassed or fail.
If student secures <= 39 marks in any subject, consider him as fail. Also assigned asubject wise grade based on the following table"""
def pass_fail():
    a=input("are you present or absent in exam?chhose any one:")
    if a=="present":
       print("student is present in exam.")
    else:
       print("student is absent in exam.")
       print("Grade:NA")
    maths=int(input("Enter maths mark:"))
    physics=int(input("Enter physics mark:"))
    python=int(input("Enter python mark:"))
    sumofmarks= maths+physics+python
    avg = sumofmarks/3
    if avg>=0 and avg<=39:
        print("Grade:F")
    elif avg>=40 and avg<=44:
        print("Grade:P")
    elif avg>=45 and avg<=49:
        print("Grade:C")
    elif avg>=50 and avg<=54:
        print("Grade:B")
    elif avg>=55 and avg<=59:
        print("Grade:B+")
    elif avg>=60 and avg<=69:
        print("Grade:A")
    elif avg>=70 and avg<=79:
         print("Grade:A+")
    else:
        print("Grade:O")
pass_fail()
