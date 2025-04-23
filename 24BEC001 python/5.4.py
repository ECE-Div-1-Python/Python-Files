import random
list = []
for i in range(0,30):
    list.append(random.randrange(-50,50))

P = []
N = []
for i in list:
    if(i>=0):
        P.append(i)
    else:
        N.append(i)
print("Positive number : ",P)
print("Negative number : ",N)
