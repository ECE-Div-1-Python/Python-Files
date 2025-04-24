def check_area_vs_perimeter(length, breadth):
    
    area = length * breadth
    perimeter = 2 * (length + breadth)

    
    if area > perimeter:
        return "Area is greater than Perimeter"
    elif area < perimeter:
        return "Perimeter is greater than Area"
    else:
        return "Area and Perimeter are equal"

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))


result = check_area_vs_perimeter(length, breadth)
print(result)
