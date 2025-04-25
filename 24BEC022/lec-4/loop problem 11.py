import math
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def sin(a):
    sine=0
    for i in range(0,50):
        s=(-1)**(i)
        sine+=s*(a**(2*i+1)/factorial(2*i+1))
    return sine

x=int(input("enter the value of x:"))
a=x*math.pi/180

print(sin(a))