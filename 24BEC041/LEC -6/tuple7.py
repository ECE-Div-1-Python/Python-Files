def piplup():
    x=('kaju','carrot','badam')
    y=list(x)
    for i in y:
        if i=='carrot':
            y.remove(i)
    z=tuple(y)
    print(z) 
piplup()

