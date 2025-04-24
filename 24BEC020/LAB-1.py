def addition():
    a = 5
    b = 3
    print(a + b)

def subtraction():
    a = 10
    b = 4
    print(a - b)

def multiplication():
    a = 6
    b = 7
    print(a * b)

def division():
    a = 20
    b = 4
    print(a / b)

def alloperation():
    a = 8
    b = 2
    print(a + b, a * b, a - b, a / b)

def hours_to_minutes():
    hours = 2
    print(hours * 60)

def minutes_to_hours():
    minutes = 180
    print(minutes / 60)

def dollars_to_rs():
    dollars = 10
    print(dollars * 48)

def rs_to_dollars():
    rupees = 480
    print(rupees / 48)

def dollars_to_pound():
    dollars = 10
    rupees = dollars * 48
    pounds = rupees / 70
    print(pounds)

def grams_to_kg():
    grams = 2000
    print(grams / 1000)

def kg_to_grams():
    kgs = 2
    print(kgs * 1000)

def bytes_conversion():
    bytes = 1048576
    print(bytes / 1024, bytes / (1024**2), bytes / (1024**3))

def celsius_to_fahrenheit():
    celsius = 25
    fahrenheit = (9/5 * celsius) + 32
    print(fahrenheit)

def fahrenheit_to_celsius():
    fahrenheit = 77
    celsius = 5/9 * (fahrenheit - 32)
    print(celsius)

def simple_interest():
    P = 1000
    R = 5
    N = 2
    I = P * R * N / 100
    print(I)

def square_area_perimeter():
    L = 4
    area = L ** 2
    perimeter = 4 * L
    print(area, perimeter)

def rectangle_area_perimeter():
    L = 5
    B = 3
    area = L * B
    perimeter = 2 * (L + B)
    print(area, perimeter)

def circle_area():
    R = 7
    area = 22/7 * R * R
    print(area)

def triangle_area():
    H = 6
    L = 8
    area = H * L / 2
    print(area)

def net_salary():
    gross = 50000
    allowance = gross * 0.10
    deduction = gross * 0.03
    net_salary = gross + allowance - deduction
    print(net_salary)

def net_sales():
    gross_sales = 100000
    discount = gross_sales * 0.10
    net_sales = gross_sales - discount
    print(net_sales)

def average_marks():
    s1 = 85
    s2 = 90
    s3 = 80
    total = s1 + s2 + s3
    average = total / 3
    print(total, average)

def swap_values():
    a = 10
    b = 20
    a, b = b, a
    print(a, b)







