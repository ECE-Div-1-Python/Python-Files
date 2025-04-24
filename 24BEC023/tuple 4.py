def tuple4():
 fooditems = [("Pizza", 49),("Burger", 108),("Pasta", 80 )]
 for x in fooditems:
     print(x)
     print(sorted(fooditems))
     import operator
 print(sorted(fooditems,key=operator.itemgetter(1),reverse=True))

tuple4()
