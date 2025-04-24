def swapvalues():
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    
    a, b = b, a
    
    print(f"After swapping: a = {a}, b = {b}")

swapvalues()
