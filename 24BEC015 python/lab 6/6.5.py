l1 = [(),(1,2),(),(3,4)]
print("Original list : ", l1)
for i in l1:
    if(isinstance(i,tuple)):
        if(len(i)==0):
            l1.remove(i)
print("modify list : ", l1)