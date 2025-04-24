def factoraial(no):
    fact = 1
    for i in range(no,0,-1):
        fact = fact*i
    print(no,"!",fact)
factoraial(5)

no = 2
value = no-(no**3)/factoraial(3)+(no**5)/factoraial(5)
print(value)