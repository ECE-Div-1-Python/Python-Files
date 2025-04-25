a=int(input("Enter age\n"))

if(a<0):
    print("Enter a valid age\n")
    if(a>18):
        print("You are a major\n")
    else:
        print("You are a minor\n")