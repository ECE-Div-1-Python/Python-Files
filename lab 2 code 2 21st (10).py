import math

def check_point_in_circle(x0, y0, radius, x, y):
    distance = math.sqrt((x - x0)**2 + (y - y0)**2)
    
    if distance < radius:
        return "Inside the circle"
    elif distance == radius:
        return "On the circle"
    else:
        return "Outside the circle"

center_x = float(input("Enter the x-coordinate of the center: "))
center_y = float(input("Enter the y-coordinate of the center: "))
radius = float(input("Enter the radius of the circle: "))

point_x = float(input("Enter the x-coordinate of the point: "))
point_y = float(input("Enter the y-coordinate of the point: "))

result = check_point_in_circle(center_x, center_y, radius, point_x, point_y)
print(result)
