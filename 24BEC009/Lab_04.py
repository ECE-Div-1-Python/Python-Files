#Question 1
def q1():
    for i in range(65,91):
        print(chr(i),end=" ")
    print()
    for i in range(97,123):
        print(chr(i),end=" ")
    print()
q1()


#Question 2
def q2():
    n=int(input("Enter the number:"))
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")
q2()
#Question 3
def q3():
    str=input("Enter a string:")
    c=0
    b=0
    for i in str:
        if(i.isalpha()==True):
            c=c+1
        elif(i.isdigit()==True):
            b=b+1
    print(f"The number of alphabets in the given string is {c}")
    print(f"The number of digits in the given string is {b}")
q3()


#Question 4
def d4(n):  
    if n < 2:
        return False 
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False 
    return True 

a = int(input("Enter any number: "))  
print("Given number is Prime:", d4(a)) 

def d42(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
            
    return sum==n
a=int(input("enter a number :"))

if d42(a):
    print(a,"is a perfect number")
else:
    print(a,"is a not perfect number")

def d43(n):
    num=str(n)
    num_digits=len(num)
    sum_of_power=0

    for digit in num:
        sum_of_power+=int(digit)**num_digits

    return sum_of_power == n

a=int(input("enter any number :"))

if d43(a):
    print(a,"is an armstrong number")
else:
    print(a,"is not an armstrong number")

def d44(n):
    return str(n)==str(n)[::-1]

a=int(input("enter any number:"))

if d44(a):
    print(a,"is pelindrome")
else:
    print(a,"is not pelindrome")


def d45(n):
    square = n**2
    return str(square).endswith(str(n))

num=int(input("enter any number:"))

if d45(num):
    print(num,"is an automorphic number")
else:
    print(num,"is not an automorphic number")


#Question 5
def find_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):  
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= limit:
                triplets.append((a, b, int(c)))
    return triplets


limit = 30
triplets = find_pythagorean_triplets(limit)


for triplet in triplets:
    print(triplet)

#Question 6
def print_24_hour_format():
    for hour in range(24):
        if (hour == 0):
            print("12 Midnight")
        elif (hour < 12):
            print(f"{hour} AM")
        elif (hour == 12):
            print("12 Noon")
        else:
            print(f"{hour - 12} PM")


print_24_hour_format()

#Question 7
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
n_fact = 1
for i in range(1, n + 1):
 n_fact *= i
r_fact = 1
for i in range(1, r + 1):
 r_fact *= i
n_r_fact = 1
for i in range(1, n - r + 1):
 n_r_fact *= i
nCr = n_fact // (r_fact * n_r_fact)
nPr = n_fact // n_r_fact
print("The nCr is",nCr)
print("The nPr is",nPr)

#Question 8
def d8():
    num=int(input("enter any number :"))
    fact=1
    for i in range(1,num+1):
        fact*=i
    print("factorial of",num,"is",fact)
d8() 

#Question 9
def d9():
    n=int(input("Enter the Number:"))
    for i in range(n,0,-1):
          print(i)
d9() 

#Question 10
def d10():
 N = int(input("Enter the number: "))  
 a, b = 0, 1  
 print("Fibonacci series:")  
 for i in range(N):  
    print(a, end=" ")  
    a, b = b, a + b  
d10()

#Question 11
def d11():
    import math
    x = float(input("Enter x in radians: "))
    sin_x = math.sin(x)
    print(f"sin({x}) = {sin_x}")
d11()
