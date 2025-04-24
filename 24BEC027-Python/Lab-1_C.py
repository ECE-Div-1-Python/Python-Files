
#Question 1
def ls1():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    c=a+b
    print(f"The sum of {a} and {b} is {c}")

#Question 2
def ls2():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    c=a-b
    print(f"The substaction of {a} and {b} is {c}")

#Question 3
def ls3():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    c=a*b
    print(f"The multiplication of {a} and {b} is {c}")

#Question 4
def ls4():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    c=a/b
    print(f"The division of {a} and {b} is {c}")

#Question 5
def ls5():
    a = 10
    b = 10
    c = a+b
    print(c)
    d = a-b
    print(d)
    e = a*b
    print(e)
    f=a/b
    print(d)

#Question 6
def ls6():
    hours=int(input("Enter the number of hours:"))
    minutes=hours*60
    print(f"{hours} hours is equal to {minutes} minutes")

#Question 7
def ls7():
    minutes=int(input("Enter the number of minutes:"))
    hours=minutes/60
    print(f"{minutes} minutes is equal to {hours} hours")

#Question 8
def ls8():
    dollars=int(input("Enter the amount in dollars:"))
    Rs=dollars*48
    print(f"{dollars} dollars is equal to {Rs} rupees")

#Question 9
def ls9():
    Rupees=int(input("Enter the amount in rupees:"))
    dollars=Rupees/48
    print(f"{Rupees} Rupees is equal to {dollars} dollars")

#Question 10
def ls10():
    dollars=int(input("Enter the amount in dollars:"))
    pound=dollars*48/70
    print(f"{dollars} dollars is equal to {pound} pound")

#Question 11
def ls11():
    grams=int(input("Enter the amount in grams:"))
    Kg=grams/1000
    print(f"{grams} grams is equal to {Kg} kilograms")

#Question 12
def ls12():
    Kg=int(input("Enter the amount in kilograms:"))
    grams=Kg*1000
    print(f"{Kg} kilograms is equal to {grams} grams")

#Question 13
def ls13():
    byte=int(input("Enter in bytes:"))
    kb=byte/1024
    mb=kb/1024
    gb=mb/1024
    print(f"{byte} bytes is equal to {kb} kilobyte")
    print(f"{byte} bytes is equal to {mb} kilobyte")
    print(f"{byte} bytes is equal to {gb} kilobyte")

#Question 14
def ls14():
    celcius=int(input("Enter the temperature in degree celcius:"))
    fahrenheit=(9*celcius/5)+32
    print(f"{celcius} *c is equal to {fahrenheit} *f")

#Question 15
def ls15():
    fahrenheit=int(input("Enter the temperature in degree fahrenheit:"))
    celcius=5/9*(fahrenheit-32)
    print(f"{fahrenheit} *f is equal to {celcius} *c")

#Question 16
def ls16():
    p=int(input("Enter the value of p:"))
    r=int(input("Enter the value of r:"))
    n=int(input("Enter the value of n:"))
    i=p*r*n/100
    print(i)

#Question 17
def ls17():
    l=int(input("Enter the length of square:"))
    area=l*l
    perimeter=4*l
    print(f"Area of square of length {l} is {area}")
    print(f"Perimeter of square of length {l} is {perimeter}")

#Question 18
def ls18():
    l=int(input("Enter the length of rectangle:"))
    b=int(input("Enter the breath of rectangle:"))
    area=l*b
    perimeter=2(l+b)
    print(f"Area of rectangle of length {l} is {area}")
    print(f"Perimeter of rectangle of length {l} is {perimeter}")

#Question 19
def ls19():
    r=int(input("Enter the radius of the circle:"))
    a=22/7*r*r
    print(f"Area of the circle is {a}")

#Question 20
def ls20():
    h=int(input("Enter the height of the triangle:"))
    l=int(input("Enter the length of the triangle:"))
    a=h*l/2
    print(f"Area of the triangle is {a}")

#Question 21
def ls21():
    gs=int(input("Enter the gross salary:"))
    al = 10/100*gs
    de = 3/100*gs
    ns = gs+al-de
    print(f"net salary is {ns}")

#Question 22
def ls22():
    gs=int(input("Enter the gross sales:"))
    ns = gs-(10/100*gs)
    print(f"net sales is {ns}")

#Question 23
def ls23():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    c=int(input("Enter the number:"))
    sum=a+b+c
    avg=sum/3
    print(f"The average of {a},{b} and {c} is {avg}")

#Question 24
def ls24():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    print(f"The values of a and b before swapping is {a} and {b}")
    a = a+b
    b = a-b
    a = a-b
    print(f"The values of a and b after swapping is {a} and {b}")
