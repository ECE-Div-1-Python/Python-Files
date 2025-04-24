def b2():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))

    if (a > b and a > c):
        print("Largest value is:", a)
    elif (b > c):
        print("Largest value is:", b)
    else:
        print("Largest value is:", c)

   
    if (a < b and a < c):
        print("Smallest value is:", a)
    elif (b < c):
        print("Smallest value is:", b)
    else:
        print("Smallest value is:", c)

b2()  
