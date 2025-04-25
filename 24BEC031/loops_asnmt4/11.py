import math
def sin(x):
    s=0
    for i in range (0,80):
        s+=((-1)**i)*(x ** ((2*i)+1) /math.factorial(2*i+1))
    return s
num=int(input("Enter value of X in degrees to compute value of sin(x)"))
print(sin(num*(3.14159/180)))