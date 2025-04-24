price={
    'apple':30,
    'banana':50,
    'mango':40,
    'pineapple':50
}
quantity={
    'apple':1,
    'banana':4,
    'mango':2,
    'pineapple':3
}
total=sum(price[item] * quantity[item] for item in  price)
print('total: ',total)



