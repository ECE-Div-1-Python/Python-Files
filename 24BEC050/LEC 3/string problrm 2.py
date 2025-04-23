a=input("enter the string: ")
upper_case=""
lower_case=""
toggle_case=""
for char in a:
    if 'A'<=char<='Z':
        lower_case+=chr(ord(char)+32)
    else:
        lower_case+=chr(ord(char))


for char in a:
    if 'a'<=char<="z":
        upper_case+=chr(ord(char)-32)
    else:
        upper_case+=chr(ord(char))

for char in a:
    if 'A'<=char<='Z':
        toggle_case+=chr(ord(char)+32)
    elif 'a'<=char<="z":
        toggle_case+=chr(ord(char)-32)
    else:
        toggle_case+=chr(ord(char))
    
print("upper case: ",upper_case)
print("lower case: ",lower_case)
print("toggle case: ",toggle_case)

    

    

    


