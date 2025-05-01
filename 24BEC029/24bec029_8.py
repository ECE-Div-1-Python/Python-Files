
import random

# Generate a set of 10 random numbers between 15 and 45
random_numbers = {random.randint(15, 45) for _ in range(10)}

# Count numbers less than 30
count_less_than_30 = sum(1 for num in random_numbers if num < 30)

# Remove numbers greater than 35
random_numbers = {num for num in random_numbers if num <= 35}

print("Generated Set:", random_numbers)
print("Count of numbers that are less than 30 in set :", count_less_than_30)




words = ["apple", "banana", "cherry", "date", "elderberry"]
uppercase_set = {word.upper() for word in words}
print("Uppercase Set:", uppercase_set)



names ={"Alice", "Bob", "Charlie", "David", "Emma"}
names_set ={"Alice", "Bob", "Charlie", "David", "Emma"}

names_set.discard("Charlie")
names_set.add("Carlos")

names_set.discard("Alice")
names_set.discard("David")
print("The Original Set is : ",names)
print("Final Set of Names:", names_set)



names = {"Alice", "Aaron", "Andrew", "Brian", "Bella", "Ben"}


set_A = {name for name in names if name.startswith("A")}
set_B = {name for name in names if name.startswith("B")}
print("The original set is : ",names)
print("Names starting with A:", set_A)
print("Names starting with B:", set_B)
