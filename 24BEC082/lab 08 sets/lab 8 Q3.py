n=set()
n=('prapti','manya')

def addnames():
    for i in range(6):
        a=str(input("enter a name to add in set: "))
        n.add(a)

def modify():
    l=list(n)
    x=str(input('enter name to be modified: '))
    y=str(input('enter new name: '))
    for i in l:
        if i==x:
            x=y
    print(set(l))

def delete():
    