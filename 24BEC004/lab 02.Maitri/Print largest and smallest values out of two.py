#Print largest and smallest values out of two.
a=int(input('enter a number: '))
b=int(input('enter another number: '))
##if a>b:
##    print(a,'is largest\n',b,'is smallest')
##else:
##    print(b,'is largest\n',a,'is smallest')


def largest(a,b):
    if a>b:
        print(a,'is largest')
    else:
        print(b,'is largest')

def smallest(a,b):
    if a<b:
        print(a,'is smallest')
    else:
        print(b,'is smallest')

largest(a,b)
smallest(a,b)
