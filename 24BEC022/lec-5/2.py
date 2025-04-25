import random 
list1=[]
while len(list1)<20:
    i=random.randint(1,20)
    list1.append(i)
print("original list:",list1)
x=int(input("Enter the number:"))
c=0
for i in list1:
    if i==x:
        c+=1
print("count of ",x,"is",c)