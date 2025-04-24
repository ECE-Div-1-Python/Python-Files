def display(x):
    l1 = []
    for i in range(1,x+1):
         l2 = []
         l2.append(i)
         l2.append(i*i)
         l2.append(i*i*i)
         t1 = tuple(l2)
         l1.append(t1)
    return l1
n = int(input("Entre a number : "))
print(display(n))