#pythagorean triplets for side length<=30
for i in range(1,31):
    for j in range(1,i):
        for k in range(1, j):
            if i**2==(j**2+k**2):
                print(i,j,k)
