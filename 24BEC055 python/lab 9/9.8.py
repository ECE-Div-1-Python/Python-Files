def convert(str):
    s1 = set(str)
    l1 = list(s1)
    l1.sort()
    print(l1)
str = input("Enter a string : ")
convert(str)
