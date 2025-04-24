def revlist(l):
     if len(l)==0:
          return []
     else:
          return [l[-1]] + revlist(l[:-1])    
print(revlist([1,2,3]))   