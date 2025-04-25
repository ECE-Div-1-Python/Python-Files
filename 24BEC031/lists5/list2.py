import random

# RANDOM list of 20 ints
random_integers = [random.randint(1, 100) for _ in range(20)]
print("Generated list of random integers:", random_integers)

# take num to process
num = int(input("Enter a number to find its positions in the list: "))

# indeksing
pos = [i for i, val in enumerate(random_integers) if val == num]
#outputs acc to qn
if pos:
    print(f"The number {num} is found at positions: {pos}")
else:
    print(f"The number {num} is not found in the list.")

#too lazy for func yet again