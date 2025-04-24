import math
n=int(input("enter a number: "))
r=int(input("enter common difference: "))
print("permutation: ",(math.factorial(n)/math.factorial(n-r)))
print("combination: ",math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))
