#check for empty stack
def empt(stack):
    return len(stack) == 0


# push items to stack
def push(stack, item):
    stack.append(item)
    print(f"Item {item} pushed onto the stack.")


# pop item like buble
def pop(stack):
    if not empt(stack):
        popd_it = stack.pop()
        print(f"Item {popd_it} popped from the stack.")
    else:
        print("Stack is empty. Cannot pop.")


# peek stack
def peek(stack):
    if not empt(stack):
        print(f"Top item is: {stack[-1]}")
    else:
        print("Stack is empty.")


# display current stack
def display(stack):
    if not empt(stack):
        print("Current stack:", stack)
    else:
        print("Stack is empty.")


# func for menu
def menu():
    stack = []
    while True:
        print("\nMenu:")
        print("1. Push item onto stack")
        print("2. Pop item from stack")
        print("3. Peek top item of stack")
        print("4. Display stack")
        print("5. Check if stack is empty")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to push: ")
            push(stack, item)
        elif choice == '2':
            pop(stack)
        elif choice == '3':
            peek(stack)
        elif choice == '4':
            display(stack)
        elif choice == '5':
            if empt(stack):
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == '6':
            print("terminated successfully :)")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


#cal the func
menu()
