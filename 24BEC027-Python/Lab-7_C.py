def ls1():                                                      #Problem-1
    d1={1:"a",2:"B",3:"C"}
    d2={"a":1,"b":2,"c":3}
    d3={20:"T"}
    d4={**d1,**d2,**d3,}
    print(d4)

def ls2():                                                      #Problem-2
    d1={}
    d2={1:2,3:4}
    if d1=={}:
        print("empty")
    else:
        print(d1)

def ls3():                                                     #Problem-3
    dic={"D01":{"E01":25000,"E02":20000,"E03":35000},"D02":{"F01":21000,"F02":30000,"F03":23000}}
    lst1=[]
    lst2=[]
    for i in dic:
        if i=="D01":
            for j in dic[i]:
                lst1.append(dic[i][j])
        elif i=="D02":
            for j in dic[i]:
                lst2.append(dic[i][j])
    print("Minimun Salary of D01:",min(lst1))
    print("Maximum Salary of D01:",max(lst1))
    print("Minimun Salary of D02:",min(lst2))
    print("Maximum Salary of D02:",max(lst2))            

def ls4():                                                     #Problem-4
    str=input("Enter String: ")
    dic={}
    for i in str:
        a = str.count(i)
        dic.update({i:a})
    print(dic)

def ls5():                                                      #Problem-5
    price={"tomato":100,"Cabbage":100,"Brocoli":200}
    quantity={"tomato":2,"Cabbage":2.5,"Brocoli":0.5}
    for i in price:
        for j in quantity:
            if i==j:
                print(f"Price of {i} is {price[i]*quantity[j]}")
