import math
center_x=int(input("center x coords: "))
center_y=int(input("center y coords:  "))
point_x=int(input("point x coords:  "))
point_y=int(input("point y coords:  "))

radius=int(input("radius: "))

distance=math.sqrt(math.pow(center_x-point_x,2)+math.pow(center_y-point_y,2))

if(radius>distance):
    print("point is inside the circle")
elif(radius==distance):
    print("point lie on circle")
else:
    print("point lie outside the circle")

