def set1():
    s=["oiiai","chipichipi","meow","miaomao","muehehehe",]
    s1=set()
    w=''
    for i in s:
        w = ''
        for j in i:
            w+=j.upper()
        s1.add(w)
    print(s1)
set1()