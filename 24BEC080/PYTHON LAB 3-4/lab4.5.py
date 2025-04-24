def find_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):  
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= limit:
                triplets.append((a, b, int(c)))
    return triplets


limit = 30
triplets = find_pythagorean_triplets(limit)


for triplet in triplets:
    print(triplet)
