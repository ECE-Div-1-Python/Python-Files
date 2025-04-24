def check_age(age):
    if age <= 18:
        print("Minor")    
    else:
        print("Major")

age = int(input("Enter your age: "))

check_age(age)
