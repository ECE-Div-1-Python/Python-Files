# descending order of food base on price

l1 = [("pizza",100),("idle",50),("cocco",110)]
l2 = [i[1] for i in l1]
l2.sort(reverse=True)
l3 = []
for j in l2:
    for i in l1:
        if(isinstance(i,tuple)):
            if(j==i[1]):
                l3.append(i)
print("Food item and price",l1)    
print("descending price order : ",l3)