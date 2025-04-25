import random
def set2():
    s=set()
    s1=set()
    c=0
    for i in range(0,10):
        s.add(random.randint(15,45))
    for i in s:
        if i<30:
            c+=1
    for i in s:
        if i<=35:
            s1.add(i)
    print("Final set after removing numbers greater than 35: ",s1)
    print("\nNumber of numbers smaller than 30 : ",c)
set2()
