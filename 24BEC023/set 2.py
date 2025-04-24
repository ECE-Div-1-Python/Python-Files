import random
count=0
a=set(random.randint(15, 45) for i in range (11))
d=set()
for j in a:
  if j<30:
   count=count+1
for z in a:
  if z>35:
    d.add(z) 
a=a-d      
print(a)
print(count) 
