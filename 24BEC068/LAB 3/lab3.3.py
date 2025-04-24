def c3():
    str1=input("enter the first string:")
    str2=input("enter the second string:")


    if str1 in str2:
        print(f'"{str1}" is found in "{str2}"')
    elif str2 in str1:
        print(f'"{str2}" is found in "{str1}"')
    else:
        print("neighter  string is found in the other")
        
c3()
