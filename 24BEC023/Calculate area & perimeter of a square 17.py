def calculatesquareareaperimeter(): 
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    perimeter = 4 * side
    print(f"For a square with side length {side}:")
    print(f"Area = {area:.2f}")
    print(f"Perimeter = {perimeter:.2f}")

calculatesquareareaperimeter()
