class Stack:
    def __init__(self):
        self.stack = []

    
    def push(self, value):
        self.stack.append(value)
        print(f"Element {value} pushed to stack.")

    
    def pop(self):
        if len(self.stack) > 0:
            popped_value = self.stack.pop()
            print(f"Element {popped_value} popped from stack.")
        else:
            print("Stack is empty. Cannot pop.")

    
    def peek(self):
        if len(self.stack) > 0:
            print(f"Top element is {self.stack[-1]}")
        else:
            print("Stack is empty.")

    
    def display(self):
        if len(self.stack) > 0:
            print("Stack elements:", self.stack)
        else:
            print("Stack is empty.")


def menu():
    stack = Stack()
    
    while True:
        print("\n--- Stack Operations ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            value = int(input("Enter value to push: "))
            stack.push(value)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            stack.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()


