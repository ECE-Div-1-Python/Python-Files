def check_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    
    if area > perimeter:
        print("The area of the rectangle is greater than its perimeter.")
    else:
        print("The area of the rectangle is not greater than its perimeter.")

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

check_area_perimeter(length, breadth)
