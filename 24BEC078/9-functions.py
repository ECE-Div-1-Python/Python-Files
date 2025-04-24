#1.	Write a program that defines a function count_lower_upper() that accepts a string and calculates the number of uppercase and lowercase alphabets in it. 
# It should return these values as a dictionary. Call this function for some sample string
def f1(s):
    counts={"uppercase":0,"lowercase":0}
    for i in s:
        if i.isupper():
            counts["uppercase"]+=1
        elif i.islower():
            counts["lowercase"]+=1
    return counts
s="Hello I am the python code."
result=f1(s)
print(result)
"""**************************************************************************************"""
#2.	Write a program that defines a function compute() that calculates the value of n + nn + nnn + nnnn,
#  where n is digit received by the function. test the function for digits 4 to 7.
def f2(n):
    s=0
    v=n
    for i in range(4):
        s=s+n
        n=n*10+v
        print(i,n,s)
    return s   

for i in range(4,8):
    print(f2(i))
"""**************************************************************************************"""
#3.	Write a program that defines a function create_array() to create and return a 3D array whose dimensions are passed to the function.
#  Also initialize each element of this aray to a value passed to the function.
def create_array3(x,y,z,v):
    l=[]
    for i in range(x):
        m=[]
        for j in range(y):
            n=[]
            for k in range(z):
                n=n+[v]
        m.append(n)
    l.append(m)
    return l
x=int(input("How many rows you want in an array:"))
y=int(input("How many colums you want in an array:"))
z=int(input("How many z you want in an array:"))
n=int(input("Enter element:"))

a3=create_array3(x,y,z,v)
"""**************************************************************************************"""

"""**************************************************************************************"""

"""**************************************************************************************"""

"""**************************************************************************************"""

"""**************************************************************************************"""