def date_difference():
    from datetime import date

    date1 = (24, 2, 2025)
    date2 = (10, 3, 2025)

    d1 = date(date1[2], date1[1], date1[0])
    d2 = date(date2[2], date2[1], date2[0])

    print("Date 1:", date1)
    print("Date 2:", date2)

    diff = abs((d2 - d1).days)
    print("Number of days between the two dates:", diff)

date_difference()
