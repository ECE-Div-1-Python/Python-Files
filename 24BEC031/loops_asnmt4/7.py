
def PNC(n,r):
    nf=1
    nrf=1
    rf=1
    for i in range(1,n+1):
        nf *= i
    for i in range(1,n+1-r):
        nrf *= i
    for i in range(1,r+1):
        rf*=i

    ncr= nf/(rf*nrf)
    npr=nf/nrf
    print("nCr :",ncr,"\nnPr:",npr)

n=int(input("Enter N\n"))
r=int(input("Enter R\n"))
PNC(n,r)
