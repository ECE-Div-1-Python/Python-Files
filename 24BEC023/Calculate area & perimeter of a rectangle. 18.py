def calculaterectangleareaperimeter():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    
    area = length * breadth
    perimeter = 2 * (length + breadth)
    
    print(f"For a rectangle with length {length} and breadth {breadth}:")
    print(f"Area = {area:.2f}")
    print(f"Perimeter = {perimeter:.2f}")


calculaterectangleareaperimeter()
