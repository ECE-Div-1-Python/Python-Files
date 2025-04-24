def ls1():                                  #Problem-1
    word = input("Enter a word")
    num = word.count("a")+word.count("e")+word.count("i")+word.count("o")+word.count("u")+word.count("A")+word.count("E")+word.count("I")+word.count("O")+word.count("U")
    print("Number of vowels:",num)

def ls2():                                  #Problem-2
    def lower(str1):
        newstr = ""
        for i in str1 :
            if 65 <=ord(i) <=90 :
                newstr= newstr+ chr(ord(i)+32)
        return newstr
    def upper(str1):
        newstr = ""
        for i in str1 : 
            if 97 <= ord(i) <= 122 :
                newstr= newstr+ chr(ord(i)-32)
        return newstr
    def toggle(str1):
        newstr = ""
        for i in str1 :
            if 65 <=ord(i) <=90 :
                newstr= newstr+ chr(ord(i)+32)
            elif 97 <= ord(i) <= 122 :
                newstr= newstr+ chr(ord(i)-32)
            else :
                newstr= newstr+ i
        return newstr
    str1 = input("Enter string :")
    newstr = toggle(str1)
    print(newstr)

def ls3():                                  #Problem-3
    str1 = input("Enter string 1: ")
    str2 = input("Enter sttring 2: ")
    if str1 in str2:
        print("String 1 is in String 2")
    elif str2 in str1:
        print("String 2 is in String 1")
    else:
        print("String are not inside each other")

def ls4():                                #Problem-4
    def rm(str1,str2):
        if str2 in str1:
            str1= str1.replace(str2,"")
            print(str1)
        else:
            print(str1)
    str1 = input("Enter string")
    str2 = input("Enter remove string")
    rm(str1,str2)
    
                  
