import random
def list3():
 random_numbers = [random.randint(1, 30) for _ in range(50)]
 unique_numbers = list(set(random_numbers))
 print("Original List:", random_numbers)
 print("List without duplicates:", unique_numbers)

list3()
