while True:
    try:
        a=int(input("enter a number: "))
        print(a)
        break
    except ValueError:
        print("you didn't enter a number")
