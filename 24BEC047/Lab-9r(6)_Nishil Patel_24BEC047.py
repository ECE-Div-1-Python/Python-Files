def neg_pos(l1,l2,idx):
    if(idx!=len(l1)):
        if(l1[idx]>=0):
            l2.append(l1[idx])
            return neg_pos(l1,l2,idx+1)
        else:
            l2.append(0)
            return neg_pos(l1,l2,idx+1)
    else:
        return l2

    '''for i in l1:
        if(i>=0):
            l2.append(i)
        else:
            l2.append(0)
    return l2'''

len_l = int(input("Enter how many element you want : "))
l1 = []
for i in range(len_l):
    y = int(input("Enter a no. between -10 to 10 : "))
    l1.append(y)
print(l1)
l2 = []
idx = 0
print(neg_pos(l1,l2,idx))