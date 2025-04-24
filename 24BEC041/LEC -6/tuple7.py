def piplup():
    x=('kaju','carrot','ditto')
    y=list(x)
    for i in y:
        if i=='carrot':
            y.remove(i)
    z=tuple(y)
    print(z) 
piplup()

