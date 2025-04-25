def pytrips():
    l=[]
    for i in range(1,31):
        for j in range(i,31):
            for k in range(j,31):
                if i*i+j*j==k*k:
                    l.append([i,j,k])
    for i in l:
        print(i)

pytrips()