import string
def lowr(S):
    s=''
    for i in S:
        if 65<=ord(i)<=90:
            s+=chr(ord(i)+32)
        else:
            s+=(i)
    return s
def uppr(S):
    s=''
    for i in S:
        if 97<=ord(i)<=122:
            s+=chr(ord(i)-32)
        else:
            s+=(i)
    return s
def togl(S):
    s=''
    for i in S:
        if 97<=ord(i)<=122:
            s+=chr(ord(i)-32)
        elif 65<=ord(i)<=90:
            s+=chr(ord(i)+32)
        else:
            s+=(i)
    return s


S=input("Enter a string to display it in lowercase, uppercase and togglecase : \n")
print("Lowercase : ",lowr(S))
print("Uppercase : ",uppr(S))
print("Togglecase : ",togl(S))
