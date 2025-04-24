#nCr = n!/(n-r)!r! and nPr = n!/(n-r)!
def factorial(x):
    fact = 1
    for i in range(x,0,-1):
        fact *= i
    return fact

n = int(input("Enter n for nCr and nPr : "))
r = int(input("Enter r for nCr and nPr : "))
nCr = factorial(n)/(factorial(n-r)*factorial(r))
print(nCr)
nPr = factorial(n)/factorial(n-r)
print(nPr)