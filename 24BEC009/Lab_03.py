def q1():
    ''''string=input("Enter the string")
    x=string.count(a)
    y=string.count(e)
    z=string.count(i)
    w=string.count(o)
    v=string.count(u)
    print(x+y+z+w+v)'''
    a=input("Enter the string")
    c=0
    for ch in a:
        if ch in "aeiouAEIOU":
            c=c+1
    print(c)
    
def q2():
    def lower(str):
        str=input("Enter the string")
        newstr= ""
        for ch in str:
            if 'A'<=ch<='Z':
                newstr+=chr(ord(ch)+32)
            else:
                newstr+=ch
        print(newstr)
    def upper(str):
        str=input("Enter the string")
        newstr= ""
        for ch in str:
            if 'a' <=ch<= 'z':
                newstr+=chr(ord(ch)-32)
            else:
                newstr+=ch
        print(newstr)
    def toggle(str):
        str=input("Enter the string")
        newstr= ""
        for ch in str:
            if 'A'<=ch<='Z':
                newstr+=chr(ord(ch)+32)
            elif 'a'<=ch<='z':
                newstr+=chr(ord(ch)-32)
        print(newstr)
    toggle(str)

def q3():
    str1=input("Enter the string")
    str2=input("Enter the string")
    if(str1 in str2):
        print("The string 1 is present in string 2")
    else:
        print("String 1 is not present in string 2")

def q4():
    str1=input("Enter the string")
    str2=input("Enter the string")
    if(str1 in str2):
        sp=str1.find(str2)
        str3=str1[:sp]+str1[sp+len(str2):]
        print(str3)
q4()   
