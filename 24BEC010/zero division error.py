def try1():
    a=int(input('enter 1st number:'))
    b=int(input('enter 2nd number:'))
    try:
        print(a/b)
    except ZeroDivisionError as zde:
        print('denominator 0')
        print(zde.args)
        x=input('press a key')
        print(zde)
try1()