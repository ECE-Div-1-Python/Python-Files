#fibonacci series
n3=0
a=int(input("enter number of numbers in series: "))
n1=int(input("enter first digit of series: "))
n2=int(input("enter second digit of series: "))
for i in range(a):
    n3=n1+n2
    print(n3)
    n1,n2=n2,n3
