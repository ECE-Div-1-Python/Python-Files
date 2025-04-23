a=5
b=10
c=15
if(a>b and a>c):
    if(b>c):
        print(a,"is largest")
        print(c,"is smallest")
    else:
        print(a,"is largest")
        print(b,"is smallest")
elif(b>a and b>c):
    if(a>c):
        print(b,"is largest")
        print(c,"is smallest")
    else:
        print(b,"is largest")
        print(a,"is smallest")
elif(c>b and c>a):
    if(b>a):
        print(c,"is largest")
        print(a,"is smallest")
    else:
        print(c,"is largest")
        print(b,"is smallest")