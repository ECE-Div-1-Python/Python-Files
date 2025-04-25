s1=input("enter the string 1:  ")
s2=input("enter the string 2:  ")

if s1 in s2:
    print(s1,"is present in",s2)
elif s2 in s1:
    print(s2,"is present in",s1)
else:
    print(s1,"is not present in",s2)
    