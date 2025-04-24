def convert(n):
    s=list(str(n).lower())

    a=set(s)
    s=list(a)
    sort = sorted(s)

    return sort

n=input("enter the string: ")
print(convert(n)) 