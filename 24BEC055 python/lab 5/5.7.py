list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
list3 = []

for i in list1:
    for j in list2:
        if(j==i):
            break
    else:
        list3.append(i)
print("List1 :", list1)
print("List2 :", list2)
print("List3 :", list3)