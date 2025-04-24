def tuple2():
    i = [(1, 'DHS', 53), (2, 'DHS', 35), (9, 'DHS', 93)]
    print(i)
    rn = []
    nm = []
    age = []

    for x in i:
        print(x, '\t', x[0], x[1], x[2])
        rn.append(x[0])
        nm.append(x[1])
        age.append(x[2])

    print("Roll Numbers:", rn)
    print("Names:", nm)
    print("Ages:", age)

tuple2()
