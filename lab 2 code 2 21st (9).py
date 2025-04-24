def check_collinear(x1, y1, x2, y2, x3, y3): 
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    
    if area == 0:
        print("The points are collinear (lie on the same straight line).")
    else:
        print("The points are not collinear.")

x1 = float(input("Enter the coordinates of the first point (x1): "))
x2 = float(input("Enter the coordinates of the second point (x2): "))
x3 = float(input("Enter the coordinates of the third point (x3): "))
y1 = float(input("Enter the coordinates of the third point (y1): "))
y2 = float(input("Enter the coordinates of the third point (y2): "))
y3 = float(input("Enter the coordinates of the third point (y3): "))


check_collinear(x1, y1, x2, y2, x3, y3)