import random

odd_numbers = random.sample(range(1, 100, 2), 5)
print("Original list of 5 odd integers:", odd_numbers)

even_numbers = random.sample(range(2, 100, 2), 4)
print("List of 4 even integers:", even_numbers)

odd_numbers[2] = even_numbers
print("After replacing third element with even integers:", odd_numbers)

flattened_list = []
for item in odd_numbers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)
print("Flattened list:", flattened_list)

flattened_list.sort()
print("Sorted list:", flattened_list)

