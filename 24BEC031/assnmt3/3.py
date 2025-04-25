def chckstr(S,s):
    return(S in s)

S=input("Enter a string \n")
s=input("Enter substring to check for in the original string \n")
print(chckstr(s,S))