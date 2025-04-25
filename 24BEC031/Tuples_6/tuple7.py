def delt(tupl):
    #typecasting
    new=list(tupl)
    #deleting element
    new.pop(2)
    return(tuple(new))


tupl=(1,2,3,4,5)
print("Initial tuple :",tupl)
print("Modified tuple :",delt(tupl))