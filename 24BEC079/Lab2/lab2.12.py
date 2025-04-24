def b12():
    import math  

    
    circle_x = 0
    circle_y = 0
    radius = 7

    
    point_x = 5
    point_y = 3

    
    distance = math.sqrt(math.pow(point_x - circle_x, 2) +
                         math.pow(point_y - circle_y, 2))

    
    if distance < radius:
        print(f"The point ({point_x}, {point_y}) is inside the circle.")
    elif distance == radius:
        print(f"The point ({point_x}, {point_y}) is on the circle.")
    else:
        print(f"The point ({point_x}, {point_y}) is outside the circle.")


b12()
