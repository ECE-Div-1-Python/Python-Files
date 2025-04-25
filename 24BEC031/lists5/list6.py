#func to convert
def tocel(l):
    nl=[]
    for i in l:
        #push to new list
       nl.append((5 / 9) * (i - 32))
    return nl
#list in fah
l=[56,76,78,87,0,100]

print(tocel(l))