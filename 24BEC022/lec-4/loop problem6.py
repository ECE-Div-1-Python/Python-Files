for time in range(24):
    if (time==0):
        print("12 MIDNIGHT")
    elif (time<12):
        print(f"{time}AM")
    elif (time==12):
        print("12 noon")
    else:
        print(f"{time-12}PM")