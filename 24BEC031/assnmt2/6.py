a=int(input("Enter a number to print the number of digits in it\n"))
c=0

while a>0:
    a//=10
    c+=1
print(c)