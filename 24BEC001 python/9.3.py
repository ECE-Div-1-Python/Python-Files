row = int(input("Enter a row : "))
column = int(input("Enter a column : "))
height = int(input("Enter a height : "))
number = int(input("Enter a number : "))
def array(row,column,height,n): #row,column,height
    lr = []
    for r in range(0,row):
        lc = []
        for c in range(0,column): 
            lh = []
            for h in range(0,height):
                lh.append(n)
            lc.append(lh)
        lr.append(lc)
    return lr
print(array(row,column,height,number))