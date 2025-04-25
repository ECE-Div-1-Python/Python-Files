queue =[]

while True:
    print("\nMenu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Exit")
    choice =int(input("Enter your choice: "))

    if choice ==1:
        item =input("Enter the item to enqueue: ")
        queue.append(item)
        print(f"{item} added to queue.")
    elif choice ==2:
        if queue:
            print(f"{queue.pop(0)} removed from queue.")
        else:
            print("Queue is empty!")
    elif choice ==3:
        print("Queue:", queue)
    elif choice ==4:
        break
    else:
        print("Invalid choice!")