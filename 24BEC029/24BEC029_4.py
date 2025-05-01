import random
o=[]
for i in range(5):
    o.append(random.randrange(1,10))

            print(o)
l=[]
l1=[]
for x in range(5):
    b=input("Enter string:")
    l.append(b)
for x in l:
    y=x.upper()
    l1.append(y)
print('The original list =',l)
print('The upper case list =',l1)



l=[]
l1=[]
a=int(input("How many elements you want to enter:"))
for x in range(a):
    k=int(input("Enter temperature value in farenheit:"))
    c=5*(k-32)/9
    l.append(k)
    l1.append(c)
print("The farenheit list =",l)
print("The celsius list =",l1)


import random
l=[]
l1=[]
n=0
while(n<5):
    k=random.randint(1,100)
    if(k%2==1):
        l.append(k)
        n+=1
print("The random odd number list =",l)
n=0
while(n<4):
    k=random.randint(1,100)
    if(k%2==0):
        l1.append(k)
        n+=1
print("The random even number list =",l1)
l.insert(2,l1)
l.pop(3)
print("The 3rd list =",l)

l2=[]
for x in l:
    print(x)
    l2.extend([x])
print("The flatterned list =",l2)
l2.sort()
print("The sorted listed =",l2)


l=[]
n=int(input("Enter n number of elements :  ")) 
for i in range(0,n):
   i=input()
   l.append(i)
print("list elements are : ",l)


import random
l=[]
n=0
while(n<20):
    l.append(random.randint(1,20))
    n+=1
print("list is =",l)
a=int(input("Enter a number:"))
m=0
for y in l:
    if(y==a):
        print("One of the position is =",m)
    m+=1


import random 
l1=[]
l2=[]
for x in range(10):
    k=random.randint(1,25)
    l1.append(k)
for y in range(10):
    k=random.randint(1,25)
    l2.append(k)
l3=[i for i in l1 if i not in l2]
print("The first list is :",l1)
print("The second list is :",l2)
print("The modified list is :",l3)


import random
l=[]
for i in range(5):
    l.append(random.randint(80,100))
print(l)



import random
l=[]
n=0
while(n<10):
    k=random.randint(1,20)
    l.append(k)
    n+=1
print("Original=",l)
l1=[]
for x in range(0,len(l)):
    for y in range(x+1,len(l)):
        if(l[x]==l[y]):
            break
    else:
        l1.append(l[x])
print("The non duplicate list =",l1)
            
            
import random 
l1=[]
l2=[]
for x in range(10):
    k=random.randint(1,25)
    l1.append(k)
for y in range(10):
    k=random.randint(1,25)
    l2.append(k)
l3=[i for i in l1 if i not in l2]
print("The first list is :",l1)
print("The second list is :",l2)
print("The modified list is :",l3)


import random
l=[]
l1=[]
l2=[]
for x in range(0,30):
    k=random.randint(-50,50)
    l.append(k)
    if(k>=0):
        l1.append(k)
    else:
        l2.append(k)
print("The main list =",l)
print("The positive list =",l1)
print("The negative list =",l2)
