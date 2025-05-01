def array(a,b,c,value):
    array=[[value for i in range(c)for i in range(b)for i in range(a)]]
    return array
x=int(input("Enter Number of raws: "))
y=int(input("Enter Number of columns: "))
z=int(input("Enter vv : "))
values=int(input("Enter Values: "))
print(array(x,y,z,values))


def count_upper_lower(str):
    uppercase=0
    lowercase=0
    for ch in str:
        if ch.isupper():
            uppercase+=1
        elif ch.islower():
            lowercase+=1
    return {"Uppercase":uppercase,"Lowercase":lowercase}

sample_str=input("Enter a string : ")
result=count_upper_lower(sample_str)
print("Number of character : ",result)


def compute(n):
    n1=int(str(n))
    n2=int(str(n)*2)
    n3=int(str(n)*3)
    n4=int(str(n)*4)

    return n1+n2+n3+n4
for i in range(4,8):
    print(f"compute({i})= ",compute(i))



def sum_avg(r,s,t,u,v):
    sum=0
    avg=0
    sum=r+s+t+u+v
    avg=sum/5
    return sum,avg
print(sum_avg(1+3+5+8+9))



