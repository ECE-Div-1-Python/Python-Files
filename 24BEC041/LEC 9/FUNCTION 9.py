def count_alha_digit(n):
    s=n.lower()
    d={"alpha":0,"digits":0}
    for i in s:
        if i.isdigit():
            d['digits']+=1
        else:
            d['alpha']+=1
    print(d)
count_alha_digit(input("enter the string: "))
