import math

x1=int(input("Enter x co ordinate of center of circle\n"))
y1=int(input("Enter y co ordinate of center of circle\n"))
r=int(input("Enter the radius of the circle\n"))
x2=int(input("Enter x co ordinate of the point\n"))
y2=int(input("Enter y co ordinate of the point\n"))

d=math.sqrt((pow(x1-x2),2)+pow(y1-y2,2))

if(d>r):
    print("The point is outside the circle\n")
elif(d<r):
    print("The point is inside the circle\n")
elif(d==r):
    print("The point lies on the circle\n")
