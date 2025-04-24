price={'tamata':150,'carrot':30,'onion':60,'potato':100}
quantity={'tamata':5,'carrot':10,'onion':6,'potato':2}
for i in price:
    for j in quantity:
     if i==j:
        print(f"price of {i} is {price[i]*quantity[j]}")
