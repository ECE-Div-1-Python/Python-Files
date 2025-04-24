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

random_numbers = [random.randint(1, 50) for _ in range(20)]
print("List of 20 random integers:", random_numbers)

user_number = int(input("Enter a number to find its positions: "))
positions = [index for index, value in enumerate(random_numbers) if value == user_number]

if positions:
    print(f"The number {user_number} occurs at positions:", positions)
else:
    print(f"The number {user_number} does not occur in the list.")

random_numbers_50 = [random.randint(1, 30) for _ in range(50)]
print("List of 50 random integers:", random_numbers_50)

unique_numbers = list(set(random_numbers_50))
print("List after removing duplicates:", unique_numbers)
