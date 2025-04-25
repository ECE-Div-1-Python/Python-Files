#func to take values present in first but not second list | (selective survival) :)
def tl(ol,sl):
    trl=[i for i in ol if i not in sl]
    return trl
ol=[1,2,3,4,5,6,7,8,9,10]
sl=[1,3,5,7,9]
#print
print("list 1",ol)
print("list 2",sl)
print("Required list:",tl(ol,sl))
