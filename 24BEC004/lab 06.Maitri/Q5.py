l=[(1,),(2,3,4),(),(5,),()]
for i in l:
    if i == ():
        l.remove(i)
print(l)