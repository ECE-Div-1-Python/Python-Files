def lower(s) :

    ls = ''
    for ch in s :
        if 'A' <= ch <= 'Z' :
            ls += chr(ord(ch) + 32)
        else :
            ls += ch
    print("String in lower case: ", ls)

def upper(s) :

    us = ''
    for ch in s :
        if 'a' <= ch <= 'z' :
            us += chr(ord(ch) - 32)
        else :
            us += ch
    print("String in upper case: ", us)

def toggle(s) :
    
    ts = ''
    for ch in s :
        if 'A' <= ch <= 'Z' :
            ts += chr(ord(ch) + 32)
        elif 'a' <= ch <= 'z' :
            ts += chr(ord(ch) - 32)
        else :
            ts += ch
    print("String in toggle case: ", ts)

s = input("Enter a string: ")
lower(s)
upper(s)
toggle(s)