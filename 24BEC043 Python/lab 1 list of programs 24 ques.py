
#SP1
a=36
b=12
add=a+b
print("addition of the numbers is: ",add)


#SP2
a=23
b=45
sub=a-b
print("substraction of the numbers is: ",sub)


#SP3
a=23
b=45
multi=a*b
print("multiplication of the numbers is: ",multi)


#SP4
a=23
b=45
div=a/b
print("Division of the numbers is: ",div)

#SP5

x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))

add=x+y
sub=x-y
mul=x*y
div=x/y

print("Addition of the two user defined numbers is ",add)
print("Substraction of the two user defined numbers is ",sub)
print("Multiplication of the two user defined numbers is ",mul)
print("Divison of the two user defined numbers is ",div)


#SP6
hrs=int(input("Enter number of hours:"))
minute=hrs*60

print("minutes in",hrs,"hours is:",minute)


#SP7
minute=int(input("Enter number of minutes:"))
hrs=minute//60

print("hours in",minute,"minutes is:",hrs)

#SP8
dollar=int(input("Enter number of dollar"))
rupee=dollar*48
print("Rupees in",dollar,"Dollars are:",rupee)

#SP9
rupee=int(input("Enter number of Ruppes"))
dollar=rupee//48
print("Dollars in",rupee,"Rupees are:",dollar)


#SP10
dollar=int(input("Enter number of dollar"))
pound=dollar*70
print("Pounds in",dollar,"Dollars are:",pound)

#SP11
pound=int(input("Enter number of Pounds"))
dollar=pound//70
print("Dollars in",pound,"pounds are:",dollar)

#SP12
gm=int(input("Enter the numbe of grams="))
kgm=gm//1000
print(gm,"grams contain",kgm,"kilograms")

#SP13
kgm=int(input("Enter the numbe of kilograms="))
gm=kgm*1000
print(kgm,"kilograms contain",gm,"grams")
'

#SP14
cel=int(input("Enter Celcius"))
F=(9/5*cel)+32
print("Fahrenheit in",cel,"Celcius is",F)

#SP15
F=int(input("Enter Fahrenheit "))
C=5/9 * (F-32)
print("Celcius in",F,"Fahrenheit is",C)

#SP16
principle=int(input("Enter Principle:"))
rate=int(input("Enter Rate:"))
time=int(input("Enter time:"))

interest=(principle*rate*time)//100
print("The interest of the given figures is",interest)


#SP17
l=int(input("Enter the side length of the square "))
a=l*l
p=4*l
print("Area ofthe sqaure is ",a)
print("Perimeter of the square is ",p)


#SP18
l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of therectangle:"))
a=l*b
p=2*(l+b)
print("Area of the rectangle is ",a)
print("Perimeter of the rectangle is ",p)


#SP19
r=int(input("Enter the radius of the circle:"))
a=3.14*r*r
print("Area of the circle is ",a)


#SP20
l=int(input("Enter the length of the triangle:"))
h=int(input("Enter the heigth of the triangle:"))

a=h*l/2
print("Area of the triangle is ",a)


#SP21
gross_salary = float(input("Enter the gross salary: "))
allowance = 0.10 * gross_salary
deduction = 0.03 * gross_salary
net_salary = gross_salary + allowance - deduction
print("Net Salary: ",net_salary)


#SP22
gross_sales = float(input("Enter the gross sales: "))
discount = 0.10 * gross_sales

net_sales = gross_sales - discount

print("Net Sales: ",net_sales)


#SP23
sub1=int(input("Enter the marks of maths:"))
sub2=int(input("Enter the marks of english:"))
sub3=int(input("Enter the marks of science:"))

total_marks=sub1+sub2+sub3

avg_marks=total_marks/3

print("Total marks obtained by the student",total_marks)
print("Avergae marks obtained by the student",avg_marks)



#SP24
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))

temp=x
x=y
y=temp

print("After swapping:")
print("x = ",x)
print("y = ",y)






