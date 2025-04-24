#Question 1
def f1():
a=int(input("enter the number:"))
b=int(input("enter the number:"))
if(a>b):
    print(f"{a} is largest and {b} is smallest")
else:
    print(f"{b} is largest and {a} is smallest")
#Question 2
def f2():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    c=int(input("Ënter the number:"))
    if(a<b and a<c):
        if(b<c):
            print(f"{a} is smallest and {c} is largest")
        else:
            print(f"{a} is smallest and {b} is largest")
    elif(b<a and b<c):
        if(a<c):
            print(f"{b} is smallest and {c} is largest")
        else:
            print(f"{b} is smallest and {a} is largest")
    else:
        if(b>a):
            print(f"{c} is smallest and {b} is largest")
        else:
            print(f"{c} is smallest and {a} is largest")
#Question 3
def f3():
    y=int(input("Enter the number:"))
    if(y%2==0):
        print(y,"is the even number")
    else:
        print(y,"is odd number")
#Question 4
def f4():
    u=int(input("Enter the number:"))
    if(u%10==0):
        print(u,"is divisible by 10")
    else:
        print(u,"is not divisible by 10")
#Question 5
def f5():
    age=int(input("Enter the age of the person"))
    if(age>=18):
        print("Major")
    else:
        print("Minor")
#Question 6
def f6():
    r=(input("Enter the number:"))
    print(len(r))
#Question 7
def f7():
    year=int(input("Enter the year:"))
    if(year%4==0):
        print(year,"is the leap year")
    else:
        print(year,"is notnthe leap year")
#Question 8
def f8():
    a1=int(input("Enter the angle"))
    a2=int(input("Enter the angle"))
    a3=int(input("Enter the angle"))
    if(a1+a2+a3==180):
        print("The triangle is valid triangle")
    else:
        print("The triangle is not a valid triangle")
#Question 9
def f9():
    a4=4.6
    b1=int(a4)
    print(b1)
#Question 10
def f10():
    l=60
    b=90
    perimeter=2*(l+b)
    area=l*b
    if(area>perimeter):
        print("area is greater than perimeter")
    else:
        print("area is less than perimeter")
#Question 12
def f11():
    x1=int(input("Enter the x1 coordinate:"))
    y1=int(input("Enter the y1 coordinate:"))
    x2=int(input("Enter the x2 coordinate:"))
    y2=int(input("Enter the y2 coordinate:"))
    x3=int(input("Enter the x3 coordinate:"))
    y3=int(input("Enter the y3 coordinate:"))
    slope_1 = (y2 - y1) / (x2 - x1)
    slope_2 = (y3 - y2) /(x3 - x2)
    if(slope_1==slope_2):
        print("The points fall in a straight line!")
    else:
        print("The points does not fall in a straight line!")
#Question 12
def f12():
    x1=int(input("Enter the x coordinate of centre of the circle:"))
    y1=int(input("Enter the y coordinate of centre of the circle:"))
    x2=int(input("Enter the x coordinate of the point:"))
    y2=int(input("Enter the y coordinate of the point:"))
    r=int(input("Enter the radius of the circle:"))
    if(((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)-r*r)<0):
        print("The point lies inside the circle")
    elif(((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)-r*r)==0):
        print("The point lies on the circle")
    else:
        print("The point lies outside the circle")
#Question 13
def f13():
    n=int(input("Enter the number:"))
    if(n==0):
        print("Zero")
    elif(n==1):
        print("one")
    elif(n==2):
        print("Two")
    elif(n==3):
        print("Three")
    elif(n==4):
        print("Four")
    elif(n==5):
        print("Five")
    elif(n==6):
        print("Six")
    elif(n==7):
        print("Seven")
    elif(n==8):
        print("Eight")
    elif(n==9):
        print("Nine")
    elif(n==10):
        print("Ten")
    elif(n==11):
        print("Eleven")
    elif(n==12):
        print("Twelve")
    elif(n==13):
        print("Thirteen")
    elif(n==14):
        print("Forteen")
    elif(n==15):
        print("Fifteen")
    elif(n==16):
        print("Sixteen")
    elif(n==17):
        print("seventeen")
    elif(n==18):
        print("Eighteen")
    elif(n==19):
        print("Ninteen")
#Question 14 
def b14():
    
    s1 = int(input("Enter the math mark: "))
    s2 = int(input("Enter the chemistry mark: "))
    s3 = int(input("Enter the physics mark: "))

    
    if (s1 < 0) or (s1 > 100) or (s2 < 0) or (s2 > 100) or (s3 < 0) or (s3 > 100):
        print("Invalid marks! Please enter marks between 0 and 100.")
    else:
        if (s1 < 40) or (s2 < 40) or (s3 < 40):
            print("Fail")
        else:
            average = (s1 + s2 + s3) / 3
            if 40 <= average <= 44:
                print("P")
            elif 45 <= average <= 49:
                print("C")
            elif 50 <= average <= 54:
                print("B")
            elif 55 <= average <= 59:
                print("B+")
            elif 60 <= average <= 69:
                print("A")
            elif 70 <= average <= 79:
                print("A+")
            elif 80 <= average <= 100:
                print("O")
b14()

