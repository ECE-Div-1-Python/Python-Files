d1={
    "i1":100,
    "i2":200,
    "i3":300
}
d2={
    "i1":5,
    "i2":10,
    "i3":15
}
total=0
for i in d1.keys():
    total=total+d1[i]*d2[i]
print(total)
