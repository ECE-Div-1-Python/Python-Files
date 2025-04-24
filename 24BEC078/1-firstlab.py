# Sum of two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The sum of two numbers is {num1 + num2}")

# Hours to minutes
hour = int(input("Enter the number of hours: "))
print(f"The number of minutes in {hour} hours is {hour * 60}")

# Minutes to hours
minutes = int(input("Enter the number of minutes: "))
print(f"The number of hours in {minutes} minutes is {minutes / 60}")

# Dollar to rupees
dollars2rupee = float(input("Enter the amount in dollars: "))
print(f"{dollars2rupee} dollars is equal to {dollars2rupee * 48} rupees")

# Rupees to dollars
rupees2dollar = float(input("Enter the amount in rupees: "))
print(f"{rupees2dollar} rupees is equal to {rupees2dollar / 48} dollars")

# Dollar to pound
dollars2pound = float(input("Enter the amount in dollars: "))
print(f"{dollars2pound} dollars is equal to {dollars2pound * (70 / 48)} pounds")

# Pound to dollar
pounds = float(input("Enter the amount in pounds: "))
print(f"{pounds} pounds is equal to {pounds / (70 / 48)} dollars")

# Kilograms to grams
kilograms = float(input("Enter the weight in kilograms: "))
print(f"{kilograms} kilograms is equal to {kilograms * 1000} grams")

# Grams to kilograms
grams = float(input("Enter the weight in grams: "))
print(f"{grams} grams is equal to {grams / 1000} kilograms")

# Convert bytes to KB, MB, GB using 1 KB = 1000 bytes
bytes_value = int(input("Enter the size in bytes: "))
print(f"{bytes_value} bytes is equal to {bytes_value / 1000} KB")
print(f"{bytes_value} bytes is equal to {bytes_value / (1000 ** 2)} MB")
print(f"{bytes_value} bytes is equal to {bytes_value / (1000 ** 3)} GB")

# Convert Celsius to Fahrenheit
celsius = float(input("Enter the temperature in Celsius: "))
print(f"{celsius}°C is equal to {(celsius * 9/5) + 32}°F")

# Convert Fahrenheit to Celsius
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
print(f"{fahrenheit}°F is equal to {(fahrenheit - 32) * 5/9}°C")

# Calculate interest
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
N = float(input("Enter the time in years: "))
print(f"The interest is {(P * R * N) / 100}")

# Calculate area and perimeter of a square
side = float(input("Enter the side length of the square: "))
print(f"The area of the square is {side ** 2}")
print(f"The perimeter of the square is {4 * side}")

# Calculate area and perimeter of a rectangle
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
print(f"The area of the rectangle is {length * breadth}")
print(f"The perimeter of the rectangle is {2 * (length + breadth)}")

# Calculate area of a circle
radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle is {3.141 * (radius ** 2)}")

# Calculate area of a triangle
height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base length of the triangle: "))
print(f"The area of the triangle is {(height * base) / 2}")

# Calculate net salary
gross_salary = float(input("Enter the gross salary: "))
allowance = gross_salary * (10/100)
deduction = gross_salary * (3/100)
net_salary = gross_salary + allowance - deduction
print(f"The net salary is {net_salary}")

# Calculate net sales
gross_sales = float(input("Enter the gross sales: "))
discount = gross_sales * 0.10
net_sales = gross_sales - discount
print(f"The net sales are {net_sales}")

# Calculate average of 3 subjects along with their total
def average(a, b, c):
    total = a + b + c
    print(f"The total marks are {total}")
    print(f"The average marks are {total / 3}")

subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
average(subject1, subject2, subject3)

# Swap 2 values
value1 = input("Enter the first value: ")
value2 = input("Enter the second value: ")
value1, value2 = value2, value1
print(f"After swapping, first value is {value1} and second value is {value2}")