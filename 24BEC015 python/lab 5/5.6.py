# convert list of temp in F to C

F = [10,20,30]
C = []

for i in F:
    y =5/9*(i-32)
    C.append(y)
print("F : ",F)
print("C : ",C)