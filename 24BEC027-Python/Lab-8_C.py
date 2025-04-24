import random
def ls1():
    lst=["World","Word","Wode"]
    set=set()
    for i in lst:
        set.add(i.upper())
    print(set)

def ls2():
    s = set()
    d = set()
    count=0
    for i in range(1,11):
        s.add(random.randint(15,45))
    for i in s:
        if i>30:
            count=count+1
        if i>35:
         d.add(i)
    s=s-d   
    print(count)
    print(s)

def ls3():
    s = set()
    for i in range(1,6):
        s.add(input("Enter name: "))
    print(s)
    nm= input("Enter name to modify: ")
    if nm in s:
        newnm = input("Replace with: ")
        s.remove(nm)
        s.add(newnm)
    else :
        print(nm,"Not found")
    print(s.pop(),"is deleted")
    print(s.pop(),"is deleted")
    print("new:",s)

def ls4():
    s= {"Abhay","Bhomik","Amla","Brinjial"}
    sa=set()
    sb=set()
    for i in s:
        if i.startswith("A"):
            sa.add(i)
        elif i.startswith("B"):
            sb.add(i)
    print(sa)
    print(sb)
