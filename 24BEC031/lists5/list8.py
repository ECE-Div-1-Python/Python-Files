# empty?
def isempT(Q):
    return len(Q) == 0

# en Q [add]
def enq(queue, item):
    queue.append(item)
    print(f"Item {item} added to the queue.")

# de Q [delete]
def deq(queue):
    if not isempT(queue):
        dequeued_item = queue.pop(0)
        print(f"Item {dequeued_item} removed from the queue.")
    else:
        print("Queue is empty. Cannot dequeue.")

# Peek at Q
def peek(queue):
    if not isempT(queue):
        print(f"Front item is: {queue[0]}")
    else:
        print("Queue is empty.")

# display Q
def display(queue):
    if not isempT(queue):
        print("Current queue:", queue)
    else:
        print("Queue is empty.")

# menu func
def menu():
    q = []
    while True:
        print("\nMenu:")
        print("1. Enqueue item to queue")
        print("2. Dequeue item from queue")
        print("3. Peek front item of queue")
        print("4. Display queue")
        print("5. Check if queue is empty")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to enqueue: ")
            enq(q, item)
        elif choice == '2':
            deq(q)
        elif choice == '3':
            peek(q)
        elif choice == '4':
            display(q)
        elif choice == '5':
            if isempT(q):
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        elif choice == '6':
            print("bye :)")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

# cal menu func
menu()
