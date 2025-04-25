
def count_lower_upper(str):
    k = {"Upper": 0, "Lower": 0}
    for i in str:
        l,u=0,0
        if i.islower():
            k["Lower"]+=1
        elif i.isupper():
            k["Upper"]+=1
    return k
print(count_lower_upper(" WiWiWi "))
