while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Error: That was not a valid integer. Please try again.")

print(f"You entered a valid integer.")
