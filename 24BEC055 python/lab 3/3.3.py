# check whether one string is there in another string

def str1_in_str2(str1,str2):
    for i in range(0,len(str2)+1):
        for j in range(i,len(str2)+1):
            if(str1==str2[i:j]):
                print(str1)

str1 = input("Enter a small string  : ")
str2 = input("Enter a large string  : ")
str1_in_str2(str1,str2)