import random
import math
l1 = []
for i in range(0,10):
    i = int(random.randrange(-15,15))
    l1.append(i)
def square(n):
    return n*n
sq = map(square,l1)
print(l1)
print(list(sq))