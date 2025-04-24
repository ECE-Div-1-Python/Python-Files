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
    
































    

