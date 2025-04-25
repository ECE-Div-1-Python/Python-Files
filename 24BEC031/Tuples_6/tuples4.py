def sort(ls):
    #used selection sort
    for x in range(1,len(ls)):
        mx=x
        for y in range(mx,len(ls)):
            if ls[y][1] > ls[mx][1]:
                mx=y
        ls[mx],ls[x] = ls[x],ls[mx]
    return ls

ls=[("Appul",100),("Mengoe",70),("Ornag",80),("Kiwi",60),("Cheiri",40),("Papayaya",30)]
print(sort(ls))
