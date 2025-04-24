def tuple1():
    i=[('b1','b2','b3'),'g1','g2',('b4'),'g3']
    print(i)
    b=0
    g=0
    for x in i:
         print(x)
        if isinstance(x,tuple):
           b+=len(x)
        else:
           g+=1

print("no. of  boys :  ",b)
print("no. of  girls:  ",g)

tuple1()         
