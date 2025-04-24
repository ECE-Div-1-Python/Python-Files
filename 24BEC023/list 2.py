import random
def list2():
 random_integers = [random.randint(1, 100) for _ in range(20)]
 user_number = int(input("Enter a number to find its positions in the list: "))
 positions = [index for index, value in enumerate(random_integers) if value == user_number]

 if positions:
    print(f"The number {user_number} appears at positions: {positions}")
 else:
    print(f"The number {user_number} does not appear in the list.")

list2()
