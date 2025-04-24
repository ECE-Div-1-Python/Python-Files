# reverse a list using recursive
def rev_list(l1,l2,idx):
    if(idx!=len(l1)):
        l2.append(l1[len(l1)-idx-1])
        return rev_list(l1,l2,idx+1)
    else:
        return l2
    '''for i in range(len(l1)):
        l2.append(l1[len(l1)-i-1])
    return l2'''

l = int(input("Enter a no. of element : "))
l1 = []
for i in range(l):
    n = int(input("Enter a number : "))
    l1.append(n)
print("Original : ",l1)
l2 = []
idx = 0
print("Reversed : ",rev_list(l1,l2,idx))