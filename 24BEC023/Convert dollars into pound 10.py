def convertdollarstopounds():
    dollars = float(input("Enter the amount in dollars: ")) 
    dollartors = 48
    poundtors = 70
    pounds = dollars * (dollartors / poundtors)
    
    print(f"{dollars} dollars is equal to {pounds:.2f} pounds.")

convertdollarstopounds()
