import operator
Employee_Record=[(1,'Driti',48,'HR',19000),(2,'Rasmit',52,'HR', 22000),(3,'Krishiv',29,'HEAD',150000)]
#Filter employee by Department
dept='HR'
Filter_employee = [emp[1] for emp in Employee_Record if emp[3]==dept]
print("Ëmployees names that are in 'HR' department : ",Filter_employee)
#sort employee by Salary

salary=sorted(Employee_Record,key=operator.itemgetter(4))
print("Employees names acorrding to their salary",salary)
print("Employe name  with Highest salary: ",salary[len(salary)-1])


import datetime
date1=(30,4,2007)
date2=(30,4,2025)
d1=datetime.datetime(date1[2],date1[1],date1[0])
d2=datetime.datetime(date2[2],date2[1],date2[0])
days=abs((d2-d1).days)
print("Days between two dates : ",days)


tuple=(15,30,4,2007)
print("Original tuple : ",tuple)
tuple=(tuple[1],tuple[2],tuple[3])
print("Modified tuple: ",tuple)


tuple=(30,4,2008)
print("Original tuple : ",tuple)
tuple=(tuple[0],tuple[1],2007)
print("Modified tuple : ",tuple)


l=['G1','G2',('B1','B2'),'G3']
print(l)
boys=0
girls=0
for ele in l:
    if isinstance(ele,tuple):
        boys+=len(ele)
    else:
        girls+=1
print("The number of Boys : ",boys)
print("The number of Girls : ",girls)



tuple_lst=[(1,2),(),(30,4),(),(1,5)]
print("List : ",tuple_lst)
List=[t for t in tuple_lst if t]
print("List without empty list : ",List)


l=[(1,"Richa",17),(2,"Reni",17),(3,"Riya",18)]
print(l)
rollNumbers=[]
name=[]
age=[]
for student in l:
    rollNumbers.append(student[0])
    name.append(student[1])
    age.append(student[2])
print("Roll Numbers : ",rollNumbers)
print("Names : ",name)
print("Age : ",age)


food_items=[("Burger",449),("Pizza",759),("Sizzelers",889)]
sorted_Fooditems=sorted(food_items,key=operator.itemgetter(1),reverse=True)
print("Sorted food items : ",sorted_Fooditems)
