stack = []

while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter element to push: ")
        stack.append(element)
        print("Element pushed!")

    elif choice == 2:
        if not stack:
            print("Stack is empty!")
        else:
            print("Popped element:", stack.pop())

    elif choice == 3:
        if not stack:
            print("Stack is empty!")
        else:
            print("Stack elements:", stack)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
