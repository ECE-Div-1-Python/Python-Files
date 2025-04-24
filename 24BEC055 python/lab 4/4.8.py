# code for factorial of no.

def factoraial(no):
    fact = 1
    for i in range(no,0,-1):
        fact = fact*i
    print(no,"!",fact)
factoraial(5)