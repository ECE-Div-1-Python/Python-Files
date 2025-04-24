def modify_tuple():
    tup = (10, 20, 30, 40)
    print("Original Tuple:", tup)

    tup_list = list(tup)
    tup_list[2] = 35
    modified_tup = tuple(tup_list)

    print("Modified Tuple:", modified_tup)

modify_tuple()
