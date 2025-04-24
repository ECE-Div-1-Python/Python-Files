date = [(1,1,1),(2,2,2)]
day = 0
month = 0
year = 0
for i in date:
    if(isinstance(i,tuple)):
        for j in range(0,3):
            if(j==0):
                day = (i[j])
            elif(j==1):
                month = (i[j])
            else:
                year = (i[j])
d1 = day+(month*30)+(year*365)
print(d1)

'''
d1=int(input("Enter 1st day:"))
m1=int(input("Enter 1st month:"))
y1=int(input("Enter 1st year:"))
d2=int(input("Enter 2nd day:"))
m2=int(input("Enter 2nd month:"))
y2=int(input("Enter 2nd year:"))
l=[(d1,m1,y1),(d2,m2,y2)]
l1=[1,3,5,7,8,10,12]  # months of days 31
l2=[4,6,9,11]  # months of days 30
days=0 
y=y2-y1
if m1 in l1:
    d=31-d1+d2
elif m1 in l2:
    d=30-d1+d2
else:
    d=28-d1+d2
days+=d
for x in range(y-1):  # ont include d1 and d2 year
    days+=365
while m1!=m2:
    m1+=1
    if(m1>12):
        m1=1
        continue
    if m1 in l1:
        days+=31
    elif m1 in l2:
        days+=30
    else:
        days+=28
if y2-y1>4:
    days+=(y2-y1)//4
print("The total number of days between these 2 dates is =",days)
'''