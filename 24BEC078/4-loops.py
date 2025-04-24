#1) Print all alphabets in upper case and in lower case.
def print_alphabets():
    for i in range(65, 91):
        print(chr(i), end='')

    print()

    for i in range(97, 123):
        print(chr(i), end='')
print_alphabets()

"""----------------------------------------------------------------------------------------------------------------"""
#2) Print a multiplication table of a given number.
def table():
    n1=int(input("Enter a number:"))
    n2=int(input("Enter another number:"))
    if(n1<=n2):
        for i in range(n1,n2):
            for i in range(1,11):
                s=i*n1
                print(s)
table()        

"""----------------------------------------------------------------------------------------------------------------"""
#3) Count no. of alphabets and no. of digits in any given string.
def countalphabets():
    n=input("Enter a string:")
    count_alpha=0
    count_number=0
    for i in n:
        if i.isalpha():
            count_alpha+=1
        elif i.isdigit():
            count_number+=1
    print(f"alphabets in given string is {count_alpha}")         
    print(f"numbers in given string is {count_number}")

countalphabets()
    
"""----------------------------------------------------------------------------------------------------------------"""
#4) Check whether given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.
def isprime(s):
    if s<2:
        return False
    for i in range(2,s):
        if s%i==0:
            return False
    return True    

def is_perfect(s):
    sumofdivisors=sum(i for i in range(1,s) if s%i==0)
    return sumofdivisors==s

def is_armstrong(s):
    digit=[int(d) for d in str(s)]
    power=len(digit)
    return s==sum(d**power for d in digit)

def is_palindrome(s):
    return str(s)==str(s)[::-1]

def is_automorphic(s):
    return str(s**2).endwith(str(s))
    
s=int(input("Enter a number:"))    
print(f"{s} is prime:{isprime(s)}")
print(f"{s} is perfect:{is_perfect(s)}")
print(f"{s} is armstrong:{is_armstrong(s)}")
print(f"{s} is palindrome:{is_palindrome(s)}")
print(f"{s} is automorphic:{is_automorphic(s)}")

"""----------------------------------------------------------------------------------------------------------------"""
#5)	Generate all Pythagorean Triplets with side length <= 30.
def pythagorean_triplets():
    for a in range(1,31):
        for b in range(a,31):
            c= (a**2 + b**2)** 0.5
            if c==int(c) and c<=30:
                print(f"({a},{b},{int(c)})")
pythagorean_triplets()
    
"""----------------------------------------------------------------------------------------------------------------"""
#6)	Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight
def calculatetime():
    for hour in range(24):
        if hour==0:
            print("12 AM(Midnight)")
        elif hour==12:
            print("12 PM(Noon)")
        elif hour<12:
            print(f"{hour} AM")
        elif hour>12:
            print(f"{hour} PM")
        else:
            print(f"{hour-12} PM")
calculatetime()

"""----------------------------------------------------------------------------------------------------------------"""
#7)	Print nCr and nPr.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def nCr(n,r):
  return factorial(n)//(factorial(r)*factorial(n-r))  

def nPr(n,r):
    return factorial(n)//(factorial(n-r))  


n=int(input("Enter your n:"))
r=int(input("Enter your r:"))

print(f"nCr ({n}C{r}) = {nCr(n,r)}")
print(f"npr ({n}P{r}) = {nPr(n,r)}") 

"""----------------------------------------------------------------------------------------------------------------"""
#8)	Print factorial of a given number.
def factorial():
    n=int(input("Enter a number:"))
    f=1
    i=1
    for i in range(1,n+1):
        i+=1
        f=f*i
    print(f"Factorial of {n} is {f}")     
factorial()

"""----------------------------------------------------------------------------------------------------------------"""
#9)	Print N natural nos. in reverse
def natural_number():
    n=int(input("Enter a number:"))
    for i in range(n,0,-1):
        print(i)        
natural_number()

"""----------------------------------------------------------------------------------------------------------------"""
#10)	Generate N numbers of Fibonacci series
def fibonacci():
    n=int(input("Enter a number:"))
    f1,f2=0,1
    i=1
    print("Fibonacci series:")

    while i<=n:
        print(f1,end=" ")
        f1,f2=f2,f1+f2
        i+=1
    print()

fibonacci()   

"""----------------------------------------------------------------------------------------------------------------"""

#11)Calculate sin(x); x is a radian value. The formula is as under:sin⁡〖x=x- x^3/3!〗+  x^5/5!-  x^7/7!…sin⁡〖x=x- x^3/3!〗+  x^5/5!-  x^7/7!…
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

def sin(x,terms=4):
    sinx=0
    for n in range(terms):
        term=((-1)**n)*(x**(2*n+1))/factorial(2*n+1)
        sinx+=term
        return sinx
x=int(input("Enter value of x:"))  
sin_approx=sin(x)
print(f"Apporximate sin({x}) using taylor series:{sin_approx} ")  
    
