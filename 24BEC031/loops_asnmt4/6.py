def hrs():
    for i in range(0,24):
        
        if 12>=i>=0:
            print(i,":00")
            print("AM")
            if 4>=i>=0:
                print("Midnight")
            elif 7>=i>4:
                print("Early Morning")
            elif 9>=i>7:
                print("Morning")
            elif 12>i>9:
                print("Late Morning")
            elif i==12:
                print("Midnoon")

        elif 24>i>12:
            print(i-12,":00")
            print("PM")
            if 16>=i>12:
                print("Afternoon")
            elif 20>=i>16:
                print("Evening")
            elif 24>=i>20:
                print("Night")
hrs()