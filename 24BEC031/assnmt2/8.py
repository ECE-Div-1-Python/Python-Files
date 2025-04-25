a=int(input("Enter 3 angles of a triangle to check if it is a valid triangle\n"))
b=int(input)
c=int(input)

if(a>0 and b>0 and c>0):
    if(a==b and b==c and c==a):
        print("It is a valid triangle")
    else:
        print("The triangle is not valid")
else:
    print("Please enter positive angle values")