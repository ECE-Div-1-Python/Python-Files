s=set()
for i in range(5):
    s.add(input("enter the name:"))
print(s)
nm=input("enter the name to modify:") 
if nm in s:
    newnm=input("replace it with ",input(""))
    s.remove(nm)
    s.add(newnm)    
else:
    print(nm," not found")
print(s.pop,"is deleted")
print(s.pop,"is deleted")
print("the final list",s)
