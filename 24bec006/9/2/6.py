def q6():
    def sanitize(lst:list,index=0):
        if(index==len(lst)):
            return lst
        if(lst[index]<0):
            lst[index]=0
        sanitize(lst,index+1)
    
    numbers=list(map(int,input("Enter the numbers space seprated: ").split()))
    sanitize(numbers)
    print("The sanitized list is",numbers)
q6()