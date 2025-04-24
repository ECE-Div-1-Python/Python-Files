queue = []

while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter element to enqueue: ")
        queue.append(element)
        print("Element added!")

    elif choice == 2:
        if not queue:
            print("Queue is empty!")
        else:
            print("Removed element:", queue.pop(0))

    elif choice == 3:
        if not queue:
            print("Queue is empty!")
        else:
            print("Queue elements:", queue)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
