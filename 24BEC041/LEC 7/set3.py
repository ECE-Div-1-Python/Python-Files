list=[]

for i in range(5):
    list.append(input("Enter a name: "))



s=set(list)

print("The list is: ",s)

nv=input("Enter a name to remove: ")
if nv in list:
    list.remove(nv)
    list.append(input("Enter a new name: "))
else:
    print("Name not found")
print(list.pop(),"is deleted")
print(list.pop(),"is deleted")

print(set(list))


