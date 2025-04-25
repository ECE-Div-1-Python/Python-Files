import random 
list1=[]
c=0
while len(list1)<10:
    i=random.randint(15,45)
    list1.append(i)

for el in list1:
    if el>=35:
        list1.remove(el)
    if el<30:
        c+=1
set=set(list1)
        

print(set)
print(c)