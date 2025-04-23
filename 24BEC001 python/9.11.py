def create_list(l1,l2):
    l3 = []
    for i in l1:
        for j in l2:
            if(i==j):
                l3.append(i)
    return l3
l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]
print(create_list(l1,l2))