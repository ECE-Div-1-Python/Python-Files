def compute(n,m):
    a=0
    for i in range(n,m+1):
        for j in range(1,i+1):
            a+=(i**j)
        print(a)
compute(4,7)
    
        
