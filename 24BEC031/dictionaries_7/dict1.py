#defined a function for the question
def d1():
    #defined dictionaries and initialized 3 of them
    d={}
    d1={'x':1,'y':2,'z':3}
    d2={'a':1,'b':2,'c':3}
    d3={'p':1,'q':2,'r':3}
    #updated dictionary d with all three dictionaries
    d.update(d1)
    d.update(d2)
    d.update(d3)
    return d
#called the function into a print statement to print the final dictionary
print(d1())