x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))
x3=int(input("x3: "))
y3=int(input("y3: "))

m1=(y2-y1)/(x2-x1)
m2=(y3-y2)/(x3-x2)

if(m1==m2):
    print("points are collinear")
else:
    print("points are not collinear")


