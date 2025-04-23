a=input("enter the string: ")
str=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in a:
    if i in str: 
        count+=1
print("vowels present in string: ",count)
