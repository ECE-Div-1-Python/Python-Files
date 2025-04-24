
def prime(n,d=2):
    if n<=1:
        return[]
    if n%d==0:
        return [d]+prime(n//d,d)
    else:
        return prime(n,d+1)
n=int(input("enter the number: "))
print(prime(n))
