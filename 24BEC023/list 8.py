class Queue:
    def __init__(self):
        self.queue = []

   
    def enqueue(self, value):
        self.queue.append(value)
        print(f"Element {value} added to the queue.")

   
    def dequeue(self):
        if len(self.queue) > 0:
            dequeued_value = self.queue.pop(0)  # Remove from the front
            print(f"Element {dequeued_value} removed from the queue.")
        else:
            print("Queue is empty. Cannot dequeue.")

    
    def peek(self):
        if len(self.queue) > 0:
            print(f"Front element is {self.queue[0]}")
        else:
            print("Queue is empty.")

    # Display all elements in the queue
    def display(self):
        if len(self.queue) > 0:
            print("Queue elements:", self.queue)
        else:
            print("Queue is empty.")


def menu():
    queue = Queue()
    
    while True:
        print("\n--- Queue Operations ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display Queue")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            value = int(input("Enter value to enqueue: "))
            queue.enqueue(value)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.peek()
        elif choice == 4:
            queue.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()
