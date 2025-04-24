def vowelcount(s,i=0,c=0):
    if i>=len(s):
        return c
    elif s[i] in 'aeiouAEIOU':
        c+=1
    return vowelcount(s,i+1,c)
print(vowelcount('manya'))