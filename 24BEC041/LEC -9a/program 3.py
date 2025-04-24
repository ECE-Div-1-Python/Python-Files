import random
lst=[random.randint(-15,15) for i in range(10)]
square=map(lambda x:x*x,lst)
print(list(square))