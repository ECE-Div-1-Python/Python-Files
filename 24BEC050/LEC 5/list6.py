def temp(list):
    f=[(f-32)* 9/5 for f in list]
    return f
l=[100,232,323,233,445]
temp=temp(l)
print(temp)