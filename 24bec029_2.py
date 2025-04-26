a=int(input("Enter value of a : "))
print(a)
b=int(input("Enter value of b : "))
print(b)
if(a>b):
 print("a is Largest and b is smallest ")
else:print(" b is Largest and a is smallest")


a=int(input("Enter value of a :"))
print(a)
b=int(input("Enter value of b :"))
print(b)
c=int(input("Enter value of c :"))
print(c)
if(a>b and a>c):
    print("a is Largest and b,c are smallest")
if(b>a and b>c):
    print("b is Largest and a,c are smallest")
if(c>a and c>b):
    print("c is Largest and a,b are smallest")
      
a=int(input("Enter value of a :"))
if(a%2==0):
    print("a is even")
else:print("a is odd")


a=int(input("Enter a Number:"))
if(a%10==0):
    print("A number is divisible by 10")
else:print("A number is not divisible by 10")


age=int(input("Enter The Age:"))
if(age<18):
    print("Minor")
else:print("Major")    


year=int(input("Enter a year :"))
if(year%4==0 and year%100!=0):
    print("It is a leap year")
else:
    print("It is not a leap year")


a=int(input("Enter The 1st angle of a triangle:"))
b=int(input("Enter The 2nd angle of a triangle:"))
c=int(input("Enter The 3rd angle of a triangle:"))
if(a+b+c==180):
    print("Triangle is valid")
else:print("Triangle is not valid")


year=int(input("Enter a year :"))
if(year%4==0 and year%100!=0):
    print("It is a leap year")
else:
    print("It is not a leap year")


length=int(input("Enter length of a rectangle : "))
breadth=int(input("Enter breadth of a rectangle : "))
area=length*breadth
perimeter=2*(length+breadth)
print("Area of rectangle is",area)
print("Perimeter of rectangle is",perimeter)
if(area>perimeter):
            print("Area of rectangle is greater than it's perimeter")
else:
    print("Area of rectangle is not greater than it's perimeter")



x1=int(input("Enter 1st x cocordinate X1:"))
y1=int(input("Enter 1st y cocordinate y1:"))
x2=int(input("Enter 2nd x cocordinate X2:"))
y2=int(input("Enter 2nd y cocordinate y2:"))
x3=int(input("Enter 3rd x cocordinate X3:"))
y3=int(input("Enter 3rd y cocordinate y3:"))
d1=((x2-x1)**2+(y2-y1)**2)**1/2
d2=((x3-x2)**2+(y3-y2)**2)**1/2
d3=((x3-x1)**2+(y3-y1)**2)**1/2
if d3==d1+d2:
    print("Given points are colinear")
else:
    print("Given points are not colinear")


x=int(input("Enter x-coordinte of center : "))
y=int(input("Enter y-coordinte of center : "))
a=int(input("Enter x-coordinte of point : "))
b=int(input("Enter y-coordinte of point : "))
radius=int(input("Enter Radius of circle : "))
distance =(((x-a)**2+(y-b)**2)**(1/2))
if(distance<radius):
    print("Point is inside of the circle")
if(distance==radius):
    print("Point is on the circle")
if(distance>radius):
    print("Point is outside of the circle")


a=int(input("Enter a number : "))#between 0 to 19

words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
             "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
             "Seventeen", "Eighteen", "Nineteen"]
if(a<20):
  print(words[a])
else:
    print("Invalid input")


sub1=int(input("Entere marks of sub 1 : "))
sub2=int(input("Entere marks of sub 2 : "))
sub3=int(input("Entere marks of sub 3 : "))
total = sub1+sub2+sub3
print("Total marks =",total)
Avg = total/3
print("Avg = ",Avg)
#if(sub1=Absent):
   # print("NA")
if(0<=sub1<=39):
    print("sub 1 = F")
if(40<=sub1<=44):
    print("sub 1 = P")
if(45<=sub1<=49):
    print("sub 1 = C")
if(50<=sub1<=54):
    print("sub 1 = B")
if(55<=sub1<=59):
    print("sub 1 = B+")
if(60<=sub1<=69):
    print("sub 1 = A")
if(70<=sub1<=79):
    print("sub 1 = A+")
if(80<=sub1<=100):
    print("sub 1 = O")
if(0<=sub2<=39):
    print("sub 2 = F")
if(40<=sub2<=44):
    print("sub 2 = P")
if(45<=sub2<=49):
    print("sub 2 = C")
if(50<=sub2<=54):
    print("sub 2 = B")
if(55<=sub2<=59):
    print("sub 2 = B+")
if(60<=sub2<=69):
    print("sub 2 = A")
if(70<=sub2<=79):
    print("sub 2 = A+")
if(80<=sub2<=100):
    print("sub 2 = O")
if(0<=sub3<=39):
    print("sub 3 = F")
if(40<=sub3<=44):
    print("sub 3 = P")
if(45<=sub3<=49):
    print("sub 3 = C")
if(50<=sub3<=54):
    print("sub 3 = B")
if(55<=sub3<=59):
    print("sub 3 = B+")
if(60<=sub3<=69):
    print("sub 3 = A")
if(70<=sub3<=79):
    print("sub 3 = A+")
if(80<=sub3<=100):
    print("sub 3 = O")

