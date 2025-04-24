def threepointfallononestraight ():
 x1, y1 = map(float, input("Enter coordinates of point 1 (x1 y1): ").split())
 x2, y2 = map(float, input("Enter coordinates of point 2 (x2 y2): ").split())
 x3, y3 = map(float, input("Enter coordinates of point 3 (x3 y3): ").split())

 if (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1):
    print("The points are collinear (fall on one straight line).")
 else:
    print("The points are not collinear.")

threepointfallononestraight()
