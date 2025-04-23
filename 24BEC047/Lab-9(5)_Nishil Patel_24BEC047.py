def ispangram(s1):
    if(s2.issuperset(s1)):
        print(str1,"It is pangram")
    else:
        print(str1," : It is not pangram")
str1 = input("Enter a string : ")
s1 = set(str1)
str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst "
s2 = set(str2)
print(s2)
ispangram(s1)
# The quick brown fox jumps over the lazy dog