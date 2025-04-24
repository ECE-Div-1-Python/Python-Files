import math
def sin(x):
    r=x*(3.14159/180)
    sine = 0
    for i in range(100):
        sign = (-1) ** i
        t = r ** (2 * i + 1) / math.factorial(2 * i + 1)
        sine += sign * t
    print(sine)
sin(90)