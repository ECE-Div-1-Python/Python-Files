def b13():
    n = 2  
    words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]

    if 0 <= n <= 19:
        print(f"The number {n} is written as '{words[n]}'.")
    else:
        print("Number is out of range (0-19).")


b13()
