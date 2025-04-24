def create_array(x, y, z, value):
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]
array_3d = create_array(3, 4, 5, 0)  


for i in range(len(array_3d)):
    for j in range(len(array_3d[i])):
        print(array_3d[i][j])
    print()  
