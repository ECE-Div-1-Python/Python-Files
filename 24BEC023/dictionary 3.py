info={'d01':{'e01':15000,'e02':25000},'d02':{'e01':15000,'e02':2500}}
lst1=[]
lst2=[]
for i in info:
    if i=="d01":
        for j in info[i]:
            lst1.append(info[i][j])
    elif i=="d02":
        for j in info[i]:
            lst2.append(info[i][j])
print("Minimun Salary of D01:",min(lst1))
print("Maximum Salary of D01:",max(lst1))
print("Minimun Salary of D02:",min(lst2))
print("Maximum Salary of D02:",max(lst2))
 
