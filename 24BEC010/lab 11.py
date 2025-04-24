def try2():    
    try:
        x=int(input("enter an integer: "))
    except ValueError as ve:
        print(ve)
        print('try again\n')
        try2()
try2()