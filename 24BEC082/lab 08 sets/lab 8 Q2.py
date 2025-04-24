import random
s=set()
count=0
for i in range(11):   
    s.add(random.randint(15,45))
print(s)

l=list(s)
print(l)
for i in l[:]:
    if i<30:
        count+=1
    if i>35:
        l.remove(i)
s=set(l)

print('numbers < 30:',count)
print(s)