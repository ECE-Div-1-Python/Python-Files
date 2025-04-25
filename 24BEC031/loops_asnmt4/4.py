def isPrm(num):
    c=0
    for i in range (2,num):
        if num%i==0:
            c=1
    if c==0:
        print("is prime\n")
    else:
        print("isn't prime\n")

def isPerf(num):
    sum=0
    for i in range (1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        print("is perfect\n")
    else:
        print("isn't perfect\n")

def isArm(num):
    rem=0
    sum=0
    n=num
    S=str(num)
    l=len(S)
    while(num>0):
        rem=num%10
        num=num//10
        sum+=rem**l
    if sum==n:
        print("is an armstrong number\n")
    else:
        print("isn't an armstrong number\n")

def isPal(num):
    s=str(num)
    S=s[::-1]
    if(s==S):
        print("is a palindrome\n")
    else:
        print("isn't a palindrome\n")

def isAuto(num):
    s=str(num*num)
    if str(num) == str(s[-len(str(num))::]):
        print("is automorphic\n")
    else:
        print("isn't automorphic\n")

N=int(input("Enter a number to check if it is prime, is perfect, is Armstrong, is palindrome, or is automorphic.\n"))
print(N,":\n")
isPrm(N)
isPerf(N)
isArm(N)
isPal(N)
isAuto(N)

