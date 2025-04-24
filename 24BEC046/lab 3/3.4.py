str = "hello world"
strR = "world"
str1 = ""
for i in range(0,len(str)+1):
        for j in range(0,len(str)+1):
            if(strR==str[i:j]):
                  str1 = str1 + str[0:i]
                  str1 = str1 + str[j:len(str)]   
print(str1)
                  