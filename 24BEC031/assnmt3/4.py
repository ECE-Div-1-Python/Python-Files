def rem(S,s):
    i=0
    if S in s:
        i=s.find(S)
        s=s[:i]+s[len(S)+i:]
    return s


S=input("Enter a string \n")
s=input("Enter substring to remove from the original string \n")
print(rem(s,S))