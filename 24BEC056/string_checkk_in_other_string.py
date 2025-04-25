string1=input("enter the string1:")
string2=input ("enter the string2 :")
if string1 in string2:
        print(f'"{string1}" is present in "{string2}"')
elif string2 in string1:
        print(f'"{string2}" is present in "{string1}"')
else:
        print("Neither string is present in the other.")

