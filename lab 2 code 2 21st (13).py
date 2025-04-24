a = float(input("enter 1st value: "))
b = float(input("enter 2nd value: "))
c = float(input("enter 3rd value: "))
    


if a >= b and a >= c:
    print("Largest value is", a)
elif b >= a and b >= c:
    print("Largest value is", b)
else:
    print("Largest value is", c)   


if a <= b and a <= c:
     print("smallest value is", a)
elif b <= a and b <= c:
     print("smallest value is", b)
else:
    print("smallest value is", c)

