def factorial(n):
    f=1
    for i in range(1,n+1):    
        f*=i
    return f    
         
n=int(input("enter a number: "))
r=int(input("enter common difference: "))
print("permutation: ",(factorial(n)/factorial(n-r)))
print("combination: ",factorial(n)/(factorial(n-r)*factorial(r)))