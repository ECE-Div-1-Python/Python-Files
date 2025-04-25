import random
# list of random nums generated
rannums = [random.randint(-100, 100) for _ in range(30)]
print("Generated list of 30 random numbers:", rannums)

# +ve nums list
posnum = [num for num in rannums if num > 0]
print("List of positive numbers:", posnum)

# -ve nums list
negnum = [num for num in rannums if num < 0]
print("List of negative numbers:", negnum)

#lazy for func