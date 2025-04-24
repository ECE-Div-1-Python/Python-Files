def create_list(l,m):
    x=[]
    for i in l:
        for j in m:
            if i==j:
                x.append(i)
    return x
l=[]
m=[]
length_list1=int(input("enter the length of list1: "))
length_list2=int(input("enter the length of list2: "))
for i in range(length_list1):
    l.append(int(input(f"enter the {i}  element of list1: ")))
for j in range(length_list2):
    m.append(int(input(f"enter the {j}  element of list1: ")))


print(create_list(l,m))