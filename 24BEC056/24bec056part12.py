# whether the point lie in the circle or outside the circle :
x=float(input("enter the center x coordinates of  circle"))
y=float(input("enter the center y coordinates of circle "))
r=float(input("enter the circle radius :"))

#input point coordinates 
px=float(input("enter the x-coordinate of the point :"))
py=float(input("enter the y-coordinate of the point :"))

# calculate the distance between the point and center of the circle 
distance= ((px-x)**2 + (py-y)**2)**0.5

# check the distace and radius of the circle 
if r>distance:
    print("point is lie in the circle ")
else:
    print("point lie outside the circle ")