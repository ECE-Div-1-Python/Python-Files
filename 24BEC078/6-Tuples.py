#1.	A list contains names of boys and girls as its elements. Boys’ names are stored as tuples. 
# Write a program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))
def tuple1():
    t1=["Kripa","Vidhi",("b1","b2"),"Rutvika",("b3",),"Kamyaa"]
    c1,c2=0,0
    for i in t1:
        if(isinstance(i,tuple)):
            c1+=len(i)
        else:
            c2+=1
    print("Boys no:",c1,"Girls no:",c2)
tuple1()               
"""---------------------------------------------------------------------------------------------------------------------------------------"""
#2.	A list contains tuples containing roll no., name and age of student.
#  Write a python program to create three lists separately for roll no., name and age
def tuple2():
    l1=[(78,"Kripa",18),(10,"Vidhii",18),(5,"Kamyaa",18),(29,"Rutvikaa",18)]
    roll_no=[]
    name=[]
    age=[]
    for x in l1:
        roll_no.append(x[0])
        name.append(x[1])
        age.append(x[2])
    print(roll_no,name,age)    
tuple2()
"""---------------------------------------------------------------------------------------------------------------------------------------"""
#3.	Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates.
import datetime
def tuple3():
    d1=(18,2,2025)
    d2=(18,2,2024)
    date1=datetime.date(d1[2],d1[1],d1[0])
    date2=datetime.date(d2[2],d2[1],d2[0])
    print(type(date1))
    print(abs(date1-date2))
tuple3()
"""---------------------------------------------------------------------------------------------------------------------------------------"""
#4.	Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price.
def tuple4():
    l1=[("Pizza",489),("Burger",165),("Pasta",280),("Sandwich",250)]
    for x in l1:
        print(l1)
    print(sorted(l1))
    import operator
    print(sorted(l1,key=operator.itemgetter(1),reverse=True))
tuple4()

"""---------------------------------------------------------------------------------------------------------------------------------------"""   
#5.	Remove empty tuple(s) from the list of tuples.
def tuple5():
    l1=[(1,2),(),(3,4),()]
    print(l1)
    for x in l1:
        if len(x)==0:
            l1.remove(x)
    print(l1)
tuple5()

"""---------------------------------------------------------------------------------------------------------------------------------------"""  
#6.	Modify an element of a tuple.
def tuple6():
    l1=[(1,2),(3,4),(),(5,6),()]
    print("Original list:",l1)
    for ele,x in enumerate(l1):
        if len(x)==0:
            l1.remove(x)
            l1.insert(ele,(100,))
    print(l1)
tuple6()

"""---------------------------------------------------------------------------------------------------------------------------------------"""  
#7.	Delete an element of a tuple.
def tuple7():
    my_tuple=(1,2,3,4,5)
    temp_list=list(my_tuple)
    temp_list.remove(3)
    new_tuple=tuple(temp_list)
    print(new_tuple)
tuple7()    