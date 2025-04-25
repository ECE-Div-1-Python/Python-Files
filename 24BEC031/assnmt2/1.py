a=int(input("Enter num1\n"))
b=int(input("Enter num2\n"))

if(a>b):
    print(a,"is greatest\n")
    print(b,"is smallest")
elif(a==b):
    print(a,"is equal to",b)
else:
    print(b,"is greatest\n")
    print(a,"is smallest")