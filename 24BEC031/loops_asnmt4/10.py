def fib(n):
    n1=0
    n2=1
    c=0
    while c<n:
        nt=n1+n2
        print(nt)
        n1=n2
        n2=nt
        c+=1
num=int(input("Enter an endpoint to print the fibonacci series : \n"))
fib(num)