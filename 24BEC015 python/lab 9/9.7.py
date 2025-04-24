def ispalindrome(str):
    str2 = ""
    for i in str:
        y = ord(i)
        if(y<=122 and y>=97):
            str2 = str2+i
        elif(y<=90 and y>=65):
            str2 = str2+i
    l2 = list(str2)
    l1 = []
    l1 = l1+l2
    l1.reverse()
    if(l1==l2):
        print("It is palidrome.")
str = input("Entre a string : ")
ispalindrome(str)