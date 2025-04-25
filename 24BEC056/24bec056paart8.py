#input the angles of triangle 
angle1=float(input("enter the first angle of triangle :"))
angle2=float(input("enter the second  angle of triangle :"))
angle3=float(input("enter the third angle of the triangle  :"))
#check wether it's sum is 180 or not 
sum=angle1+angle2+angle3
if sum==180 and angle1>0 and angle2>0 and angle3>0 :
    print("the triangle is valid ")
else :
    print ("the triangle is not valid .")