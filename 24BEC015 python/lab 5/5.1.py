# print 5 odd number using random nos

import random
l = []
while (len(l)<5):
    k=random.randint(1,100)
    if(k%2==1):
        l.append(k)
print("The random odd number = ",l)

# print 4 even number using random nos

l1 = []
while (len(l1)<4):
    k=random.randint(1,100)
    if(k%2==0):
        l1.append(k)
print("The random even number = ",l1)

l.insert(2,l1)
l.pop(3)
print("The 3rd list= ",l)

l2 = []
for i in l:
    print(i)
    if(isinstance(i,int)):
        l2.append(i)
    else:
        l2.extend(i)
print(l2)

l2.sort()
print(l2)

#i = []
#i.append(random.randrange(80,100,2))