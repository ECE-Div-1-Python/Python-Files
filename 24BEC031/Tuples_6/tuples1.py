def tup1():
    b=0
    g=0
    l=["maomao","mononoke","kiki","chihiro",("Neil Perry","Todd Anderson","Charlie Dalton","Knox Overstreet","Steven Meeks","Richard Cameron"), "setsuko"]
    for i in l:
        if isinstance(i,tuple):
            for j in i:
                b+=1
        else:
            g+=1
    print("No. of girls:",g,"\n No. of boys:",b)
tup1()