length=int(input("enter the length: "))
breath=int(input("enter the breath: "))
area=length*breath
perimeter=2*(length+breath)
if(area>perimeter):
    print("area is greater")
elif(area==perimeter):
    print("area and primeter are equal")
else:
   print("perimeter is greater")