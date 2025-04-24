import random

def ls1():
    odd_integers = [random.randint(1, 100) * 2 + 1 for _ in range(5)]
    even_integers = [random.randint(1, 100) * 2 for _ in range(4)]
    
    print("Original Odd Integers List:", odd_integers)
    print("Original Even Integers List:", even_integers)
    
    odd_integers[2] = even_integers
    print("\nAfter Replacing the Third Odd Integer with Even Integers List:", odd_integers)
    
    flat_list = [item for sublist in odd_integers for item in (sublist if isinstance(sublist, list) else [sublist])]
    flat_list.sort()
    
    print("\nFlattened and Sorted List:", flat_list)

def ls2():
    random_integers = [random.randint(1, 100) for _ in range(20)]
    print("Generated Random List:", random_integers)
    number = int(input("Enter a number to find its position in the list: "))
    
    positions = [i for i, x in enumerate(random_integers) if x == number]
    if positions:
        print(f"The number {number} is found at positions: {positions}")
    else:
        print(f"The number {number} is not found in the list.")

def ls3():
    random_numbers = [random.randint(1, 30) for _ in range(50)]
    print("Original List:", random_numbers)
    unique_numbers = list(set(random_numbers))
    print("\nList After Removing Duplicates:", unique_numbers)

def ls4():
    random_numbers = [random.randint(-30, 30) for _ in range(30)]
    print("Generated List:", random_numbers)
    
    positive_numbers = [num for num in random_numbers if num > 0]
    negative_numbers = [num for num in random_numbers if num < 0]
    
    print("\nPositive Numbers List:", positive_numbers)
    print("Negative Numbers List:", negative_numbers)

def ls5():
    strings = ["apple", "banana", "cherry", "date", "elderberry"]
    print("Original List of Strings:", strings)
    
    uppercase_strings = [s.upper() for s in strings]
    print("\nList of Strings in Uppercase:", uppercase_strings)

def ls6():
    fahrenheit_temperatures = [random.randint(30, 100) for _ in range(10)]
    print("List of Temperatures in Fahrenheit:", fahrenheit_temperatures)
    
    celsius_temperatures = [(temp - 32) * 5/9 for temp in fahrenheit_temperatures]
    print("\nEquivalent List of Temperatures in Celsius:", celsius_temperatures)

def ls7():
    stack = []
    
    while True:
        print("\nMenu:")
        print("1. Push an element onto the stack")
        print("2. Pop an element from the stack")
        print("3. Display stack")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            element = int(input("Enter an element to push: "))
            stack.append(element)
            print(f"{element} has been pushed onto the stack.")
        elif choice == 2:
            if stack:
                popped_element = stack.pop()
                print(f"{popped_element} has been popped from the stack.")
            else:
                print("Stack is empty!")
        elif choice == 3:
            print("Current Stack:", stack)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

def ls8():
    queue = []
    
    while True:
        print("\nMenu:")
        print("1. Enqueue an element")
        print("2. Dequeue an element")
        print("3. Display queue")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            element = int(input("Enter an element to enqueue: "))
            queue.append(element)
            print(f"{element} has been added to the queue.")
        elif choice == 2:
            if queue:
                dequeued_element = queue.pop(0)
                print(f"{dequeued_element} has been removed from the queue.")
            else:
                print("Queue is empty!")
        elif choice == 3:
            print("Current Queue:", queue)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

def ls9():
    list1 = [random.randint(1, 10) for _ in range(10)]
    list2 = [random.randint(1, 10) for _ in range(8)]
    print("First List:", list1)
    print("Second List:", list2)
    
    difference = [x for x in list1 if x not in list2]
    print("\nNumbers in First List but not in Second List:", difference)
