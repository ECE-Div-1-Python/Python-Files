def new(n):
    lst=[]
    t=[]
    for i in range(1,n+1):
        for j in range(1,4):
            t.append(i**j)
        lst.append(tuple(t))
        list(t)
        t.clear()

    print(lst)

new(int(input("enter the number:")))


