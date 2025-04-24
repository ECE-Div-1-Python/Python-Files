s=input("Enter the string")
d={}
for i in s:
    a=s.count(i)
    d.update({i:a})
print(d)    
