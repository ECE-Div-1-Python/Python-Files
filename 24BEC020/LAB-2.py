def square_of_number():
    a = 5
    print(a ** 2)

def cube_of_number():
    a = 3
    print(a ** 3)

def even_or_odd():
    a = 7
    print(a % 2 == 0)

def positive_or_negative():
    a = -10
    print(a > 0)

def maximum_of_two():
    a = 12
    b = 9
    print(max(a, b))

def minimum_of_two():
    a = 12
    b = 9
    print(min(a, b))

def simple_calculator():
    a = 10
    b = 5
    print(a + b, a - b, a * b, a / b)

def square_root():
    a = 16
    print(a ** 0.5)

def power_of_number():
    a = 2
    b = 3
    print(a ** b)

def divisible_by_5_and_11():
    a = 55
    print(a % 5 == 0 and a % 11 == 0)

def calculate_percentage():
    marks = 450
    total = 500
    percentage = (marks / total) * 100
    print(percentage)

def leap_year():
    year = 2024
    print((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

def sum_of_digits():
    number = 123
    total = sum(int(d) for d in str(number))
    print(total)

def reverse_number():
    number = 1234
    reverse = int(str(number)[::-1])
    print(reverse)
