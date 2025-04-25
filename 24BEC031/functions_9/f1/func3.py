def create_array(x, y, z, n):
    # creat the aray
    array = [[[n for _ in range(z)] for _ in range(y)] for _ in range(x)]
    return array

x=3
y=3
z=3
n=12
# call func to create array
result_array = create_array(x,y,z,n)

# 3D printed array
for i in range(x):
    print(f"Layer {i+1}:")
    for j in range(y):
        print(result_array[i][j])
    print()
