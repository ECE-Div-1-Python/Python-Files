#Write a program that receives an integer an input. If a string is entered instead of an integer, 
# then report an error and give another chance to user to enter an integer. Continue this process till correct input is supplied
def try1():
    while True:
        a=input("Enter a number:")
        try:
            number=int(a)
            print("You entered integer.",a)
            break 
        except ValueError:
            if not a.isdigit():
                print("Error..Please enter a integer value.")
try1()
   
