def uppercase():
 str=input("enter any string :")
 upper_case=""

 for ch in str:
     asc=ord(ch)
     if (asc>96 and asc<124):
         upper_case+=chr(asc-32)
     else:
          upper_case+=chr(asc)

 print("your given string in upper case is :",upper_case)         
        
uppercase()        
   

def lowercase():
    str = input("Enter any string: ")
    lower_case = ""

    for ch in str:
        asc = ord(ch)
        if (65 <= asc <= 90):
            lower_case += chr(asc + 32)
        else:
            lower_case += chr(asc)

    print("Your given string in lowercase is:", lower_case)


lowercase()


def togglecase():
 
    str = input("Enter any string: ")
    toggled_str = ""

    for ch in str:
        asc = ord(ch)
        if (65 <= asc <= 90):
            toggled_str += chr(asc + 32)
        elif 97 <= asc <= 122:
            toggled_str += chr(asc - 32)
        else:
            toggled_str += chr(asc)

    print("Your given string in toggle case is:", toggled_str)

togglecase()



