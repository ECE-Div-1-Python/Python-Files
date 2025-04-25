def create_array(x, y, z, value):
    l=[[[value]*z for _ in range(y)]for _ in range(x)]
    return l

array = create_array(3, 4, 5, 7)
for layer in array:
    for row in layer:
        print(row)
    print()



