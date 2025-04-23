x = 2   #given code
y = 1
x0 = 0 #center coordinate
y0 = 0
radius = 2
if(((x-x0)**2 + (y-y0)**2)<=(radius**2)):
    print("x =",x,"y =",y,"point lies inside circle.")
else:
    print("x =",x,"y =",y,"point not lies inside circle.")