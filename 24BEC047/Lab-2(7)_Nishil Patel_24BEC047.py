year = int(input("enter a year : "))
if(year%100==0):
    if(year%400==0):
        print(year,"is leap year")
    else:
        print(year,"is not leap year")
elif(year%4==0):
    print(year,"is leap year")
else:
    print(year,"is not leap year")