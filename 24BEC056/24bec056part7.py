#accept the year value from the user and check whether it is leap year or not 
year=int(input("enter the year :"))
print(f"the year is :",year)
if year%4==0:
    print(f"year is leap year",year)
else :
    print (f"it is not leap year ",year)