#Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if te sum of all the three angles is equal to 180 degrees.
a=int(input('enter first angle: '))
b=int(input('enter second angle: '))
c=int(input('enter third angle: '))
if a+b+c==180:
    print('valid triangle')
else:
    print('invalid triangle')