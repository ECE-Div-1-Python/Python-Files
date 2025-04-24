def q1():
    l = []  
    def primeFactors(n: int, i=2):
        if n <= 1:  
            print(l)
            return
        while n % i == 0:
            l.append(i)
            n //= i  
        primeFactors(n, i + 1)  

    num = int(input("Enter a number: "))  
    primeFactors(num)

q1()
