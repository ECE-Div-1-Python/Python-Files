# remove duplication interger in list

import random

list = []
for i in range(0,50):
    list.append(random.randint(1,30))
print(list)

list1 = []
for i in range(0,len(list)):
    for j in range(0,i):
        if(list[j]==list[i]):
            break
    else:
        list1.append(list[i])
print("Remove Dulpicate list :", list1)