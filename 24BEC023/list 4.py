import random
def list4():
 random_numbers = [random.randint(-100, 100) for _ in range(30)]
 positive_numbers = [num for num in random_numbers if num > 0]
 negative_numbers = [num for num in random_numbers if num < 0]

 print("Generated Random Numbers:", random_numbers)
 print("Positive Numbers:", positive_numbers)
 print("Negative Numbers:", negative_numbers)

list4()
