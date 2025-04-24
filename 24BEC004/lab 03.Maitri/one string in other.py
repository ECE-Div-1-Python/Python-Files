#Accept two strings. Check whether one string is there in another string
s=str(input('enter a string: '))
a=str(input('enter another string to be searched in string: '))
c=0
if a in s:
    c+=1
if c>0:
    print(a,'is in string',s)
else:
    print(a,'not in',s)