import random
#func to remove dupliket
def duplrem(nums):

    unique_numbers = list(set(nums))
    return unique_numbers

#Generate random nums
nums = [random.randint(1, 30) for _ in range(50)]
print("Generated list of random numbers :", nums)
print("List of unique numbers:", duplrem(nums))