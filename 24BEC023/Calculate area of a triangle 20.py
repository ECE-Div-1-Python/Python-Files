def calculatetrianglearea():
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))  
    area = (base * height) / 2
    
    print(f"The area of a triangle with base {base} and height {height} is: {area:.2f}")


calculatetrianglearea()
