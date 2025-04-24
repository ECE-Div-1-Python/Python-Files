def find_digit_type(number):
    if number < 10:
        print("Single digit")
    elif number < 100:
        print("Double digit")
    elif number < 1000:
        print("Triple digit")
    elif number < 10000:
        print("Four digit")
    elif number < 100000:
        print("Five digit")
    else:
        print("Number has more than five digits")

num = int(input("Enter a number: "))

find_digit_type(num)
