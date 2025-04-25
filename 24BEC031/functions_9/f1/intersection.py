def create_list(list1, list2):
    #typecaste to list
    its = list(set(list1) & set(list2))
    return its

list1 = [1, 2, 3, 4, 5,100]
list2 = [4, 5, 6, 7, 8,3]
inlt = create_list(list1, list2)
print(f"Intersection of the lists: {inlt}")
