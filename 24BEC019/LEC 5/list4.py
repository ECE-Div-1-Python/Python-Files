import random 
list1=[]
while len(list1)<30:
    i=random.randint(-100,100)
    list1.append(i)
list2=[]
list3=[]
for i in list1:
    if i<0:
        list2.append(i)
    else:
        list3.append(i)
print("negative list:",list2)
print("positive list:",list3)