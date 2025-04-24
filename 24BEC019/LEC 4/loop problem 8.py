def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("enter the value of n:"))

print(f"factorial of {n} is {factorial(n)}")