def convertnumberintoequivalentwords ():
 numberwords = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", 
    "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

 number = int(input("Enter a number between 0 and 19: "))

 if (0 <= number <= 19):
    print(f"The word equivalent of {number} is: {numberwords[number]}")
 else:
    print("Invalid input! Please enter a number between 0 and 19.")

convertnumberintoequivalentwords ()
convertnumberintoequivalentwords ()
