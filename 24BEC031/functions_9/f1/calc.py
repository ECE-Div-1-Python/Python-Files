def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b

a=int(input("Enter A :\n"))
b=int(input("Enter B :\n"))
op=input("Enter Operation\n")
if op=="+":
    print(add(a,b))
elif op=="-":
    print(sub(a,b))
elif op=="*":
    print(mul(a,b))
elif op=="/":
    print(div(a,b))
elif op=="%":
    print(rem(a,b))
