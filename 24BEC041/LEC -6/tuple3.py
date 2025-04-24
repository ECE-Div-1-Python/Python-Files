
import datetime
def tuple3():
    d1=(23,2,2006)
    d2=(19,10,2007)
    date1=datetime.datetime(d1[2],d1[1],d1[0])
    date2=datetime.datetime(d2[2],d2[1],d2[0])
    print(type(date1))
    print("Total days: ",abs(date2-date1))

tuple3()

    

