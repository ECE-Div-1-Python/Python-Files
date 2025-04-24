s1 = input("Enter a string : ")
ci = 0
ca = 0
for i in s1:
    y = ord(i)
    if(y<=57 and y>=48):
        ci += 1
    if((y<=122 and y>=97) or (y<=90 and y>=65)):
        ca += 1
print("No. of digit in string : ", ci)
print("No. of alphabet in stinrg : ", ca)