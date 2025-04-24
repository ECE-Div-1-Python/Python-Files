def b11():
    x1 = 1
    x2 = 3
    x3 = 5
    y1 = 2
    y2 = 6
    y3 = 10
    a = (x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))
    
    if (a == 0):
        print('All the points fall on one straight line')
    else:
        print("All the points do not fall on one straight line")

b11()
