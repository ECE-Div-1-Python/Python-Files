def delete_tuple_element():
    tup = (10, 20, 30, 40)
    print("Original Tuple:", tup)

    tup_list = list(tup)
    del tup_list[1]
    modified_tup = tuple(tup_list)

    print("Tuple after deleting element:", modified_tup)

delete_tuple_element()
