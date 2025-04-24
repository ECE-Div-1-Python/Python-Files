def b1():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    if (a > b):
        largest = a
        smallest = b
    else:
        largest = b
        smallest = a

    
    print("Largest value is:", largest)  
    print("Smallest value is:", smallest)  

b1()
