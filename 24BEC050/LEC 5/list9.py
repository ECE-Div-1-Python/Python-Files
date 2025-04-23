def difference_list(list1, list2):
    return [item for item in list1 if item not in list2]


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6]
result = difference_list(list1, list2)
print(result)
