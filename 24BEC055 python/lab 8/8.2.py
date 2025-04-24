import random
l1 = []
for i in range(0,10):
    l1.append(random.randrange(15,45))
print(l1)
s1 = {i for i in l1}
print(s1)
count = 0
for i in s1:
    if(i<=30):
        count += 1
print("Number less than 30 : ",count)
l2 = list(s1)
for i in l2:
    if(i>=35):
        l2.remove(i)
s2 = set(l2)
print(s1)