import random
list1=[]
list2=[]
while len(list1)<5:
    i=random.randint(1,200)
    if i%2!=0:
        list1.append(i)
while len(list2)<4:
    i=random.randint(1,200)
    if i%2==0:
        list2.append(i)
print("odd list: ",list1)
print("even list:",list2)
list1.pop(2)
list1.insert(2,list2)
print("new list:",list1)
list1.pop(2)
for i in range(0,4):
    list1.insert(i+2,list2[i])
print("flatten list:",list1)
print("sortten list:",sorted(list1))












