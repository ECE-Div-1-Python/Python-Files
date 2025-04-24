import datetime
import operator
def ls1():                              #Problem-1
    ls=[("Khantil","Nishil","Yaksh","Shyam"),"Sanjana","Maya","Riya"]
    c1=0
    c2=0
    for i in ls:
        if isinstance(i,tuple):
            for j in i:
                c1=c1+1
        else:
            c2=c2+1
    print("No. of girls:",c2)
    print("No. of boys:",c1)

def ls2():                          #Problem-2
    ls=[("24BEC027","Khantil",18),("24BEC027","GanShyam",5),("24BEC047","Nishil",18)]
    roll=[]
    name=[]
    age=[]
    for i in ls:
        if isinstance(i,tuple):
            for j in i:
                if str(j).isalpha():
                    name.append(j)
                elif str(j).isdigit():
                    age.append(j)
                else :
                    roll.append(j)
    print(roll)
    print(name)
    print(age)

def ls3():                              #Problem-3
    d1=(12,2,23)
    d2=(12,4,24)
    date1=datetime.date(d1[2],d1[1],d1[0])
    date2=datetime.date(d2[2],d2[1],d2[0])
    print(abs(date1-date2))

def ls4():                              #Problem-4
    ls= [("Bhel",45),("Pizza",200),("Samosa",20)]
    print(sorted(ls, key = operator.itemgetter(1)))

def ls5():                              #Problem-5
    ls=[(1,2),(),()]
    for i in ls:
        l=len(i)
        if len(i)==0:
            ls.remove(i)
    print(ls)
def ls6():                            #Problem-6
    tp=(1,2,3,4,5)
    lst_tp=list(tp)
    lst_tp.pop(2)
    lst_tp.insert(2,"Three")
    tp=tuple(lst_tp)
    print(tp)

def ls7():                            #Problem-7
    tp=(1,2,3,4,5)
    md_tp=set(tp)
    md_tp.pop()
    md_tp=tuple(md_tp)
    print(md_tp)
