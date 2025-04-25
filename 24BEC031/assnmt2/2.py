a=int(input("Enter num1\n"))
b=int(input("Enter num2\n"))
c=int(input("Enter num3\n"))
if(a>b and a>c):
    print(a,"is greatest\n")
    if(b>c):
        print(c,"is smallest\n")
    else:
        print(b,"is the smallest\n")
elif(b>c and b>a):
    print(b,"is greatest")
    if(a>c):
        print(c,"is smallest\n")
    else:
        print(a,"is the smallest\n")
elif(c>b and c>a):
    print(c,"is greatest")
    if(b>a):
        print(a,"is smallest\n")
    else:
        print(b,"is the smallest\n")