t1 = (1,5,3,4)
print("Original tuple : ",t1)
l1 = list(t1)
l1[1] = 2
t1 = tuple(l1)
print("Modify tuple : ",t1)