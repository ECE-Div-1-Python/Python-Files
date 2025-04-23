# upper case without function

str = "Hello world"
str1 = ""
for i in str:
    y = ord(i)
    if(y<=123 and y>=97):
        y = y - 32
    str1 = str1+chr(y)
print(str1)

# lower case without function

str1 = "Hello world"
str2 = ""
for i in str1:
    y1 = ord(i)
    if(y1<=90 and y1>=65):
        y1 = y1 + 32
    str2 = str2 + chr(y1)
print(str2)