#Print largest and smallest values out of three
a=int(input('enter first number: '))
b=int(input('enter second number: '))
c=int(input('enter third number: '))

def largest(a,b,c):
    m=a
    if b>m:
        m=b
    if c>m:
        m=c
    print('largest number: ', m)

def smallest(a,b,c):
    n=a
    if b<n:
        n=b
    if c<n:
        n=c
    print('smallest number: ', n)

largest(a,b,c)
smallest(a,b,c)
