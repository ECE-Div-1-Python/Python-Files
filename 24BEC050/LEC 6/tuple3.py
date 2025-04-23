"""def days():
    t1=(23,2,2006)
    t2=(19,10,2007)

    if t2[2]>t1[2]:
         y=(t2[2]-t1[2])*365
    else:
        y=(t1[2]-t2[2])*365
    if t2[1]>t1[1]:
         x=(t2[1]-t1[1])*30
    else:
        x=(t1[1]-t2[1])*30
    if t2[0]>t1[0]:
         a=(t2[0]-t1[0])
    else:
        a=(t1[0]-t2[0])
    
    print("Total days: ",y+x+a)
days()"""
import datetime
def tuple3():
    d1=(23,2,2006)
    d2=(19,10,2007)
    date1=datetime.datetime(d1[2],d1[1],d1[0])
    date2=datetime.datetime(d2[2],d2[1],d2[0])
    print(type(date1))
    print("Total days: ",abs(date2-date1))

tuple3()

    

