""" Functions to find the summition
            x
        +  xx
       +  xxx
      +  xxxx
     = ______
     where x can be any integer
"""
def addvals(num):
    sum=0
    tv=num
    for i in range(4):
        sum=sum+tv
        tv=tv*10+num

    return sum
n=int(input("Enter a number : "))
print(addvals(n))
