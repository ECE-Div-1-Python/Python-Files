d1 = {"apple": 10, "banana": 20, "mango": 30}  #fruit and price
d2 = {"apple": 30, "banana": 20, "mango": 10}  #fruit and quantity
bill = 0
l1 = []
l2 = []
for i,(f,q) in enumerate(d1.items()):
    l1.append(q)
for i,(f,q) in enumerate(d2.items()):
    l2.append(q)
for i in range(len(l1)):
    bill += l1[i]*l2[i]    
print(bill)