import math
def sum(a,b):
    return a+b
l1=[1,2,3,4,5,6]
l2=[6,5,4,3,2,1]
s = map(sum,l1,l2)   # add element with same index
print(list(s))