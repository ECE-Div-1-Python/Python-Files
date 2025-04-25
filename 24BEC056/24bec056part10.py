#area anr perimeter of the rectangle 
length=float(input("enter the length of the rectangle :"))
breath =float(input("enter the breath of a rectangle  :"))
area = (length)*(breath)
perimeter=(2)*(length+breath)
print("area of the rectangle is :",area)
print("perimeter of the rectangle is :",perimeter )
if area>perimeter:
    print("area of the rectangle is greater then the perimeter of the rectangle ")
else:
    print("area of the rectangle is not greater then the perimeter of the rectangle " )