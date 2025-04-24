import random
l=[random.randint(-15,15) for _ in range(10)]
print(l)
m=map((lambda x:x**2),l)
print(m)