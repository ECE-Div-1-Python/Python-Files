#find average of list using recursion
def avg(l1,sum,idx):
    if(idx!=len(l1)):
        sum += l1[idx]
        return avg(l1,sum,idx+1)
    else:
        return sum/len(l1)
    
    '''for i in l1:
        sum += i
    return sum/len(l1)'''

len_l = int(input("Enter how many element you want : "))
l1 = []
for i in range(len_l):
    y = int(input("Enter a number : "))
    l1.append(y)
print(l1)
sum = 0
idx = 0
print("Average : ",avg(l1,sum,idx))