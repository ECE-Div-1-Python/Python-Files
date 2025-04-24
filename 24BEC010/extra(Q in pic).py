l=[(101,'amit',35,'HR',10000),(102,'vidhi',34,'HR',20000),(103,'manya',33,'marketing',30000)

def filterbydept():
    nd=[]
    n=str(input('enter department:'))
    for i in l:
        if i[3]==n:
            nd.append(i[1])
    print(nd)

filterbydept()

def sortbysalary():
    s=[]
    for i in l:
        
   
