#Question 1
def q1():
    l=["ganga","Yamuna","sarasvati",("Dhoni","Rohit","Virat")]
    a=0
    b=0
    for i in l:
        if(isinstance(i,tuple)):
            for c in i:
                a+=1
        else:
            b+=1
    print(f"No of boys in the list are {a}")
    print(f"No of girls in the list are {b}")
#Question 2
def q2():
    l=[(7,"Dhoni",43),(45,"Rohit",37),(18,"Virat",36)]
    l1=[]
    l2=[]
    l3=[]
    for i in l:
        print(i,'\t',i[0],i[1],i[2])
        l1.append(i[0])
        l2.append(i[1])
        l3.append(i[2])
    print(l1) 
    print(l2)
    print(l3) 
#Question 3
def q3():
    import datetime
    d1=(18,2,2025)
    d2=(18,2,2024) 
    date1=datetime.date(d1[2],d1[1],d1[0])
    date2=datetime.date(d1[2],d1[1],d1[0])
    print(type(date1))
    print(abs(date1-date2))
#Question 4
def q4():
    l=[("Chips",10),("Chocolate",5),("Coke",20)]
    for i in l:
       print(i)
    print(sorted(tuple))
    import operator
    print(sorted(tuple,key=operator.itemgetter(1)))
#Question 5
def q5():
    l=[(1,2),(),(3,4),()]
    print("Original List=",l)
    for x in l:
        if len(x==0):
            l.remove(x)
    print(l)
q5()
#Question 6
def modify_tuple():
    tup = (10, 20, 30, 40)
    print("Original Tuple:", tup)

    tup_list = list(tup)
    tup_list[2] = 35
    modified_tup = tuple(tup_list)

    print("Modified Tuple:", modified_tup)

modify_tuple()
#Question 7
def delete_tuple_element():
    tup = (10, 20, 30, 40)
    print("Original Tuple:", tup)

    tup_list = list(tup)
    del tup_list[1]
    modified_tup = tuple(tup_list)

    print("Tuple after deleting element:", modified_tup)

delete_tuple_element()
