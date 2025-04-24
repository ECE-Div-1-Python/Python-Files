def remove_empty_tuples():
    tuples = [(), (1, 2), (), (3, 4, 5), (), (6,)]
    print("Original List:", tuples)

    non_empty_tuples = [t for t in tuples if t]

    print("List after removing empty tuples:", non_empty_tuples)

remove_empty_tuples()
