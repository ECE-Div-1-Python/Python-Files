def tuple5 () :
 l=[(1,2),(),(3,4),()]
 print("original list=",l)
 for x in l:
  if len(x)==0:
     l.remove(x)
 print(l)


tuple5()
