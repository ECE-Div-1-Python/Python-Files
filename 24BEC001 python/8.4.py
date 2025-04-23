n=int(input("How many records you want to enter : "))
l=[]
for x in range(n):
    k=input("Enter a name which starts either from A or B : ")
    l.append(k)
s=set(l)
print("The main set =",s)
l1=[]
l2=[]
for y in s:
    if(y[0]=="A" or y[0]=="a"):
        l1.append(y)
    else:
        l2.append(y)
s1=set(l1)
s2=set(l2)
print("The A set = ",s1)
print("The B set = ",s2)