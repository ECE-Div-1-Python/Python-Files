def PNC(n):
    nf=1
    for i in range(1,n+1):
        nf *= i
    return nf

n=int(input("Enter a number to print it's factorial\n"))

print("Factorial of N is:",PNC(n))