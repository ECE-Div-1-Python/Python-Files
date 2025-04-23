# code for N fibonacci series

a = int(input("Enter a first no. : "))
b = int(input("Enter a second no. : "))
c = int(input("Enter a no. of terms : "))
for i in range(1,c+1):
    d = a+b
    print(d)
    a = b
    b = d