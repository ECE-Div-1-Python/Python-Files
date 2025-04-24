#Question 1
import random
def q1():
    l=["dhoni","kohli","rohit"]
    s=set()
    for i in l:
        s.add(i.upper())
    print(s)
#Question 2
def q2():
    s=set()
    d=set()
    for i in range(1,11):
        s.add(random.randint(15,45))
    print(s)
    a=0
    for i in s:
        if(i<30):
            a+=1
    print(f"Number of digits less than 30 in the set = {a}")
    for i in s:
        if(i>35):
            d.add(i)
    s=s-d
    print(f"set after deleting the elements {s}")
#Question 3
def q3():
    s=set()
    for i in range(1,6):
       s.add(input("Enter the name:"))
    print(s)
    name=input("Enter the name which is to be modified:")
    for i in range(1):
        newname=input("Enter the name:")
    if(name in s):
        s.remove(name)
        s.add(newname)
    s.pop()
    s.pop()
    print(s)
#Question 4
def q4():
    s=("angad","akaay","ahan","bhupendra","Virat","anushka")
    s1=set()
    s2=set()
    for i in s:
        if(i.startswith('a')):
            s1.add(i)
    for i in s:
        if(i.startswith('b')):
            s2.add(i)
    print(s1)
    print(s2)
q4()   
