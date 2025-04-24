def PRIME(n):
    count=0
    for i in range(2,n):
        if n%i!=0:
            count=1
        else:
            count=0
    if count==1:
        print('number is prime')
PRIME(19)

def ARMSTRONG(n):
    s=str(n)
    l=len(s)
    r=0
    for i in s:
        r+=(int(i)**l)
    if r==n:
        print('number is armstrong')

def PALINDROME(n):
    s=str(n)
    if n==int(s[::-1]):
        print('number is palindrome')

def  PERFECT(n):
    a=0
    for i in range(1,n):
        if n%i==0:
            a+=i
    if n==a:
        print('number is perfect')

#def AUTOMORPHIC(n):
#    last digits of square of a number = the number