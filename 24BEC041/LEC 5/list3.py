import random 
list1=[]
while len(list1)<51:
    i=random.randint(1,30)
    list1.append(i)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("original list:",list1)
print("unique list:",list2)
