def numberoddigits ():
 number = input("Enter a number: ")
 numofdigits = len(number) if number.isdigit() or (number[0] == '-' and number[1:].isdigit()) else "Invalid input"


 if isinstance(numofdigits, int):
    print(f"The number of digits in the number is: {numofdigits}")
 else:
    print(numofdigits)

    
numberoddigits ()
