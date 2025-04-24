#1.	Write a program that converts words present in a list into uppercase and stores them in a set.
def set1():
    list=input("Enter a sentence:").split()
    s=set(list)
    s={x.upper() for x in list}
    print(s)
set1()
"""-----------------------------------------------------------------------------------------------------------------------------------"""
#2.	Write a program to create a set containing 10 random numbers in the range 15 to 45.
#Count how many of these numbers are less than 30. Delete all numbers that are greater than 35.
import random
def set2():
   s=set()
   while len(s)!=10:
       x=random.randint(15,45)
       s.add(x)
   print(s)
   d=set()
   c=0
   for x in s:
       if x<30:
           c+=1
       else:
           d.add(x)
   s=s-d         
   print("No. of elements<30",c)
   print("deleted values which are greater than 35",d)

set2()    

"""-----------------------------------------------------------------------------------------------------------------------------------"""
#3.	Create an empty set. Write a program that adds five new names to this set,
#modifies one existing name and deletes two names from it.       
def set3():
    s=set()
    for i in range(5):
        s.add(input("Enter name:"))
    print(s)
    nm=input("Enter a name to modify:")
    if nm in s:
        newnm=input("Replace it with:")
        s.remove(nm)
        s.add(newnm)
    else:
        print(nm,"not found")
    print(s.pop(),"is deleted")
    print(s.pop(),"is deleted")
    print("The final list:",s)

set3()
        

"""-----------------------------------------------------------------------------------------------------------------------------------"""
#4.	A set contains names which begin either with A or with B. Write a program to separate out the names into two
#sets, one containing names beginning with A and another with B.
def set4():
    s={"Ami","Anajali","Bijal","Bindu","Kripa"}
    sa=set()
    sb=set()
    for nm in s:
        if nm[0]=='A':
            sa.add(nm)
        elif nm[0]=='B':
            sb.add(nm)
    print(sa)
    print(sb)

set4()
    

"""-----------------------------------------------------------------------------------------------------------------------------------"""