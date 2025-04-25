def mod(tupl):
    #typecasting
    new=list(tupl)
    #modded 3rd element
    new[2]=500
    return(tuple(new))


tupl=(1,2,3,4,5)
print("Initial tuple :",tupl)
print("Modified tuple :",mod(tupl))
