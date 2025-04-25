def remtup(tuplist):
    newl=[]
    for i in tuplist:
        # giving the tuple an existential crisis if it doesn't hold value
        if i:
            newl.append(i)
    return newl
#lacking creativity
tuplist=[('miau','mau'),(),('miau','mau'),(),('miau','mau')]
print(remtup(tuplist))