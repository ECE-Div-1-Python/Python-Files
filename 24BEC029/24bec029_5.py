for hour in range(0,24):
    if(hour==0):
        print("12 Midnight")
    elif(hour<12):
        print(f"{hour}AM")
    elif(hour==12):
        print("12 Noon")
    else :
        print(f"{hour-12}PM")
        
import math
degree=int(input("Enter an angle in degree : "))
x=degree*math.pi/180
sin(x)==0
term=0
for i in range(term):
    power=2*i+1
    term=((-1)**i)*(x**power)/math.factorial(power)
sin(x)==sin(x)+term
printf("Value of sin(x) is : ",sin(x))


num=int(input("Enter the Number : "))
fact=i=1
while(i<=num):
    fact=fact*i
    i=i+1
print("Factorial of given number is : ",fact)


n=int(input("Enter a number for get elements of Fibonacci series: "))
a=0
print(a)
b=1
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a,b=b,c
    

a=int(input("Ënter a number :"))
for i in range(1,11):
 b=a*i
 print(b)


n=int(input("Enter the value of N : "))
for i in range(n,0,-1):
      print(i)


n=int(input("Enter value for n : "))
r=int(input("Enetr value for r : "))
fact=i=1
while(i<=n):
    fact=fact*i
    i = i+1
numerator = fact
sub=n-r
fact=fact*i
i=i+1
while(i<=sub):
    fact=fact*i
    i=i+1
denominator=fact
fact=i=1
while(i<=r):
    fact=fact*i
    i=i+1
denominator=denominator*fact
comb=numerator/denominator
print("\n nCr = ",comb)



n=int(input("Enter the value of n : "))
r=int(input("Enter the value of r : "))

fact=i=1
while(i<=n):
    fact=fact*i
    i=i+1
numerator = fact
sub = n-r

fact=i=1
while(i<=sub):
    fact=fact*i
    i=i+1
denominator=fact
perm=numerator/denominator
print("nPr is : ",perm)



a=int(input("Enter a number : "))
for i in range(1,a+1):
    if(i*i==a):
        print("Ä number is perfact")
        break
else:
    print("A number is not perfact")




a=int(input("Enter a number : "))
for i in range(1,a+1):
    if(i*i==a):
        print("Ä number is perfact")
        break
else:
    print("A number is not perfact")



triplets=[]
for a in range(1,20):
    for b in range(a,20):
        for c in range(b,20):
            if(a**2+b**2==c**2):
                triplets.append((a,b,c))
print(triplets)
