def list9():
 list1 = [10, 20, 30, 40, 50, 60]
 list2 = [20, 40, 60] 
 list3 = [num for num in list1 if num not in list2]


 print("List1:", list1)
 print("List2:", list2)
 print("List3 (Numbers from List1 not in List2):", list3)

list9()
