def triplets(limit):
    triplet=[]
    for a  in range(1,limit+1):
        for b in range(a,limit+1):
            c=(a**2+b**2)**0.5
            if c.is_integer() and c<=limit:
                triplet.append((a,b,int(c)))
    return triplet 
limit=30
for triplets in triplets(limit) :
    print(triplets)
    