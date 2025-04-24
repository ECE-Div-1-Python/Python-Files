def pointliesinsidethecircle ():
 import math

 xcenter, ycenter = map(float, input("Enter the coordinates of the circle's center (x y): ").split())
 radius = float(input("Enter the radius of the circle: "))
 xpoint, ypoint = map(float, input("Enter the coordinates of the point (x y): ").split())

 distance = math.sqrt(pow(xpoint - xcenter, 2) + pow(ypoint - ycenter, 2))


 if (distance < radius):
    print("The point lies inside the circle.")
 elif (distance == radius):
    print("The point lies on the circle.")
 else:
    print("The point lies outside the circle.")


pointliesinsidethecircle ()
pointliesinsidethecircle ()
pointliesinsidethecircle ()
