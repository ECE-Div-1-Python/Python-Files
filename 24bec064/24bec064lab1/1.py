def q1():
    a=int(input())
    b=int(input())
    add=a+b
    print(add)
def q2():
    a=int(input())
    b=int(input())
    sub=a-b
    print(sub)
def q3():
    a=int(input())
    b=int(input())
    product=a*b
    print(product)
def q4():
    a=int(input())
    b=int(input())
    div=a/b
    print(div)
def q5():
    a=int(input())
    b=int(input())
    add=a+b
    print(add)
    sub=a-b
    print(sub)
    product=a*b
    print(product)
    div=a/b
    print(div)
def q6():
    minutes=float(input("Enter the no of minutes:"))
    hours=minutes/60
    print("The minutes in hours is",hours)
def q7():
    hours=float(input("Enter the no of hours:"))
    minutes=hours*60
    print("The hours in minutes is",minutes)
def q8():
    dollar=float(input("Enter the value of dollars:"))
    rupees=dollar*48
    print("The Dollar in Rupees is:",rupees)
def q9():
    rupees=float(input("Enter the value of Rupees:"))
    dollar=rupees/48
    print("The Rupees in Dollar is:",rupees)
def q10():
    dollar=float(input("Enter the value of dollars:"))
    pounds=70/48*dollars
    print("The value in pounds is",pounds)
def q11():
    grams=float(input("Enter the weight in grams:"))
    kilograms=grams/1000
    print("The weight in kgs is",kilograms)
def q12():
    kilograms=float(input("Enter the weight in kilograms:"))
    grams=kilograms*1000
    print("The weight in grams is",grams)
def q13():
    byte=int(input("Enter the no of bytes you want to covert"))
    Kb=byte/1024
    Mb=Kb/1024
    Gb=Mb/1024
    print("The bytes in Kb,Mb and Gb are",Kb,Mb,Gb,"respectively",sep=",")
def q14():
    C=float(input("Enter temperature in celcius"))
    F = (9/5*C) + 32
    print("The temperature in farenheit is",F)
def q15():
    F=float(input("Enter temperature in Farenheit"))
    C = 5/9*(F-32)
    print("The temperature in celcius is",C)
def q16():
    P=float(input("Enter the principal amount"))
    R=float(input("Enter the Rate of intrest"))
    N=float(input("Enter the duration of loan in years"))
    I = P*R*N/100
    print("The Intrest amount is Rs",I)
def q17():
    side=float(input("Enter the length of square"))
    A=side**2
    P=4*side
    print("The Area of square is",A)
    print("The Perimeter of square is",P)
def q18():
    length=float(input("Enter the length of rectangle"))
    width=float(input("Enter the width of rectangle"))
    A=length*width
    P=2*(length+width)
    print("The Area of rectangle is",A)
    print("The Perimeter of rectangle is",P)
def q19():
    radius=float(input("Enter the radius of circle"))
    A=22/7*radius**2
    P=2*22/7*radius
    print("The Area of circle is",A)
    print("The Perimeter of circle is",P)
def q20():
    base=float(input("Enter the base of triangle"))
    height=float(input("Enter the height of triangle"))
    A=base*height/2
    print("The area of triangle is",A)
def q21():
    gross_salary=float(input("Enter the gross salary"))
    allowance=0.1*gross_salary
    deduction=0.03*gross_salary
    NetSalary=gross_salary + allowance - deduction
    print("The Net salary is ",NetSalary)
def calculate_total_and_average(maths, physics, chemistry):
    total = maths + physics + chemistry
    average = total / 3
    return total, average
maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
total, average = calculate_total_and_average(maths, physics, chemistry)
print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average:.2f}")
def q24():
    a=int(input("Enter value of a"))
    b=int(input("Enter value of b"))

    a,b=b,a
    print("The value of a after swap is",a)
    print("The value of b after swap is",b)
    
