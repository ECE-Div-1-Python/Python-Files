#Question 1
import random
l1=[random.randrange(1,100,2) for i in range(5)]
print(f"List of odd numbers is {l1}")
l2=[random.randrange(0,100,2) for i in range(4)]
print(f"List of odd numbers is {l2}")
l1[2]=l2
print(l1)

#Question 2
import random
lst=[random.randint(1,100) for i in range(20)]
number=int(input("Enter a number:"))
found=False
for i,val in enumerate(lst):
    if val==number:
        print(f"Number {number} is found to be at index {i}")
        found=True
if not found:
    print(f"The Number {number} was not present in the list")

#Question 3
import random
lst=[random.randrange(1,31) for i in range(50)]
lst2=list(set(lst))
print(lst2)

#Question 4
import random
lst=[random.randint(-50,50) for i in range(30)]
print("Original List:",lst)
l1=[]
l2=[]
for i in lst:
    if(i>0):
        l1.append(i)
    else:
        l2.append(i)
print("List containing poitive numbers:",l1)
print("List containing negetive numbers:",l2)

#Question 5
strings = ["apple", "banana", "cherry", "orange", "grape"]
for i in range(len(strings)):
    strings[i]=strings[i].upper()
print(strings)

#Question 6
lst=[30,40,50,35,36]
f=list(map(lambda x:(x*9/5)+32,lst))
print(f)

#Question 7
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

#Question 8
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

#Question 9
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

list3 = [num for num in list1 if num not in list2]
print("Numbers only in the first list:", list3)

