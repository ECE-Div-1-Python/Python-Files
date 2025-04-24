import datetime
def tuple3():
    d1 = (16, 1, 2025)
    d2 = (16, 1, 2024)
    date1 = datetime.date(d1[2], d1[1], d1[0])
    date2 = datetime.date(d2[2], d2[1], d2[0])
    print(type(date1))
    diff = abs(date1 - date2)
    print("Difference:", diff)


tuple3()
