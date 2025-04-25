stack =[]
while True:
    print("\nMenu:")
    print("1. Push")
    print("2. Pop")
    print("3. Display Stack")
    print("4. Exit")
    choice =int(input("Enter your choice: "))

    if choice ==1:
        item =input("Enter the item to push: ")
        stack.append(item)
        print(f"{item} pushed to stack.")
    elif choice ==2:
        if stack:
            print(f"{stack.pop()} popped from stack.")
        else:
            print("Stack is empty!")
    elif choice ==3:
        print("Stack:", stack)
    elif choice ==4:
        break
    else:
        print("Invalid choice!")