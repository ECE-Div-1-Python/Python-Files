def countalpha(S):
    c=0
    for i in S:
        if(i.isalpha()):
            c+=1
    return c

def countdig(S):
    c=0
    for i in S:
        if(i.isdigit()):
            c+=1
    return c

S=(input(("Enter a string \n")))
print("Number of alphabets in given string : ",countalpha(S),"\nNumber of digits in given string : ",countdig(S))



