#list of meows
ls=['mau','MiAu','MEWWW','MIAAUUUU','awiwiwi']
#new list to store loud meows
newl=[]

t=''
#meow amplifier func
for x in ls:
    for y in x:
        t=t+(y.upper())

    newl.append(t)
    t=''
#meower func
print(newl)
