# take input from the user 
x1=float(input("enter the coordinates x1 :"))
x2=float(input("enter the coordinates x2:"))
x3=float(input("enter the coordinates x3:"))
y1=float(input("enter the coordinates y1:"))
y2=float(input("enter the coordinates  y2:"))
y3=float(input("enter the coordinates  y3:"))
m=(x2-x1/y2-y1)
n=(x3-x2/y3-y2)
p=(x3-x1/y3-y1)
if m==n==p :
    print("coordinates are in strait line ")
else :
    print("coordinates are in not strait line ")
