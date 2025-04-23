l1 = [("1","A","19"),("2","B","20"),("3","C","21")]
rollno = []
name = []
age = []
for i in l1:
    if(isinstance(i,tuple)):
        for j in range(0,3):
            if(j==0):
                rollno.append(i[j])
            elif(j==1):
                name.append(i[j])
            else:
                age.append(i[j])
print(l1)
print("rollno",rollno)
print("name",name)
print("age",age)

    