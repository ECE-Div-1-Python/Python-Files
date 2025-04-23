def cal_value(a,b):               #a^b
    if(b==0):
        return 1
    return a*cal_value(a,b-1)
a = int(input("Enter a number : "))
b = int(input("Enter a power : "))
print(cal_value(a,b))