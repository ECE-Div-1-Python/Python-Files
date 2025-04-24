def count_lower_upper(s):
    uc=0
    lc=0
    for i in s:
        if i.isupper():
            uc+=1
        elif i.islower():
            lc+=1
    print({'uppercase':uc,'lowercase':lc})

#main
s=str(input('enter a string: '))
count_lower_upper(s)
