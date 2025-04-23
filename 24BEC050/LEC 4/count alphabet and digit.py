a=input("enter the string:")
c1=0
c2=0
for i in a:
    if i.isalpha():
        c1+=1
    if i.isdigit():
        c2+=1
print("number of alaphabets in the string is: ",c1)
print("number of digits in  the string is: ",c2)