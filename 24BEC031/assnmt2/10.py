b=int(input("Enter length\n"))
c=int(input("Enter breadth\n"))

if((b*c)>(2*(b+c))):
    print("Area of the rectangle is greater than it's perimeter",(b*c),">",(2*(b+c)))
else:
    print("Perimeter of the rectangle is greater than its Area",(2*(b+c)),">",(b*c))