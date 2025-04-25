# Dictionary containing grocery items and their prices
gp = {
    "apple": 50,
    "banana": 20,
    "milk": 30,
    "bread": 40,
    "eggs": 60
}


gq = {
    "apple": 2,
    "banana": 5,
    "milk": 1,
    "bread": 2,
    "eggs": 1
}

tb = 0

for item in gq:
    if item in gp:
        tb += gp[item] * gq[item]


print("Total Bill Amount: ", tb)
