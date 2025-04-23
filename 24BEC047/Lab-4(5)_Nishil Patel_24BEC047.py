# code for pythagoras triplet
def pythagoras_triplet(no):
    for x in range(1,no+1):
        for y in range(1,no+1):
            for z in range(1,no+1):
                l = x**2 + y**2
                if(l==(z**2) and x<y):
                    print(x,y,z)
pythagoras_triplet(30)