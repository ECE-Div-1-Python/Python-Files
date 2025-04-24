student = [("b1",),"g1",("b2",),"g2",("b3","b4","b5"),"g3"]
boys = 0
for i in student:
    if(isinstance(i,tuple)):  # compare data type of i return true or false
        for j in i:    # goes inside tuple
            boys += 1
print("student : ",student)
print("boys : ",boys)
