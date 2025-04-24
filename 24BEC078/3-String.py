#1) Count how many vowels are there in a string. Accept the stringfrom the user
def vowels():
    string=input("Enter a string:")
    print(string.count("a")+string.count("e")+string.count("i")+string.count("o")+string.count("u")+string.count("A")+string.count("E")+string.count("I")+string.count("O")+string.count("U"))
vowels()
"""------------------------------------------------------------------------------------------------------------------------------------------------------""" 

#2) Write your own functions (without using built-in functions) toconvert all characters of a string into lower case/upper case/togglecase
def lower(str):
    newstr=""
    for ch in str:
        if 'A'<=ch<='Z':
            newstr+=chr(ord(ch)+32)
        else:
            newstr+=ch
    print(newstr)

def upper(str):
    newstr=""
    for ch in str:
        if 'a'<=ch<='z':
            newstr+=chr(ord(ch)-32)
        else:
            newstr+=ch
    print(newstr)

def toggle(str):
    newstr=""
    for ch  in str:
        if 'A'<=ch<='Z':
            newstr+=chr(ord(ch)+32)
        elif 'a'<=ch<='z':
            newstr+=chr(ord(ch)-32)  
        else:
            newstr+=ch
    print(newstr)

s=input("Enter your string:")
upper(s)
lower(s)
toggle(s)

"""------------------------------------------------------------------------------------------------------------------------------------------------------""" 
#3) Accept two strings. Check whether one string is there in another string.
def comparetwostring():
    s1=input("Enter first string:")
    s2=input("Enter second string:")
    print(s2 in s1)
comparetwostring()    
    

"""------------------------------------------------------------------------------------------------------------------------------------------------------""" 
#4) Write a function that removes one string from another string, if present.
def Removestring():
    s1=input("Enter first string:")
    s2=input("Enter another string:")
    if s2 in s1:
        sp=s1.find(s2)
        s1=s1[:sp]+s1[sp+len(s2):]
        print(s1)
        
Removestring()
    