import random
nums = random.sample(range(-15, 16), 10)
sqr = [x ** 2 for x in nums]

print("Original list:", nums)
print("List of squares:", sqr)
