#Question 1
def intinput():  
    try:
        a = int(input("Enter an integer: "))
    except ValueError:
        print("Entered value isn't an integer!")
        intinput()
    else:
        print("Program exicution done..")

intinput()  