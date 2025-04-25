def countvow(S):
    c=0
    vow={'a','A','e','E','i','I','o','O','u','U'}
    for i in S:
        if i in vow:
            c+=1
    return c

S=input("Enter a string to check for vowels\n")
print(countvow(S))