def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def ncr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))
def npr(n,r):
    return factorial(n)/factorial(n-r)
n=int(input("enter the value of n: "))
r=int(input("enter the value of r: "))
print(f"{n}C{r}={ncr(n,r)}")
print(f"{n}P{r}={npr(n,r)}")