# 1. Convert words in a list to uppercase and store them in a set
def convert_to_uppercase():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    uppercase_set = {word.upper() for word in words}
    print("Set of uppercase words:", uppercase_set)

# 2. Create a set of 10 random numbers, count those less than 30, and delete numbers greater than 35
import random

def random_set_operations():
    num_set = {random.randint(15, 45) for _ in range(10)}
    print("Generated Set:", num_set)
    
    # Count how many numbers are less than 30
    less_than_30 = sum(1 for num in num_set if num < 30)
    print(f"Numbers less than 30: {less_than_30}")
    
    # Delete numbers greater than 35
    num_set = {num for num in num_set if num <= 35}
    print("Set after removing numbers greater than 35:", num_set)

# 3. Add, modify and delete names from a set
def modify_set():
    names_set = set()
    
    # Add five names to the set
    names_set.update(["John", "Alice", "Bob", "Charlie", "David"])
    print("Set after adding names:", names_set)
    
    # Modify one name (remove old name and add new one)
    names_set.discard("Charlie")
    names_set.add("Chris")
    print("Set after modifying a name:", names_set)
    
    # Delete two names from the set
    names_set.discard("Alice")
    names_set.discard("David")
    print("Set after deleting names:", names_set)

# 4. Separate names starting with A and B into two sets
def separate_names_by_letter():
    names_set = {"Alice", "Bob", "Charlie", "Adam", "Bella", "Chris", "Brian"}
    
    set_A = {name for name in names_set if name.startswith('A')}
    set_B = {name for name in names_set if name.startswith('B')}
    
    print("Names starting with A:", set_A)
    print("Names starting with B:", set_B)
