#add 2 numbers
a=int(input("enter a number: "))
b=int(input("enter another number: "))
print("sum=",a+b)


#add,multiply,subract,divide 2 numbers
a=int(input("enter number a: "))
b=int(input("enter number b(a>b,b!=0): "))
print("sum=",a+b)
print("product=",a*b)
print("difference=",a-b)
print("quotient=",a/b)


#bytes into KB, MB and GB
b=int(input('enter bytes: '))
print('bytes to KB: ',b/1000)
print('bytes to MB: ',b/(1000**2))
print('bytes to GB: ',b/(1000**3))



#Calculate area & perimeter of a rectangle
l=float(input('enter length: '))
b=float(input('enter breadth: '))
print('area=',l*b)
print('perimeter=',2*(l+b))



#Calculate area of a circle
r=float(input('enter radius: '))
print('area=',(22/7)*r*r)


#Calculate area of a triangle
b=float(input('enter base length:'))
h=float(input('enter height: '))
print('area=',(1/2)*b*h)



#Calculate average of three subjects
a=int(input('enter first no.: '))
b=int(input('enter second no.: '))
c=int(input('enter third no.: '))
print('total: ',a+b+c)
print('average: ',(a+b+c)/3)



#Calculate net salary
#where net salary = gross salary + allowance – deduction.
#Allowances are 10% while deductions are 3% of gross salary

s=float(input('enter gross salary: '))
a=0.1*s
d=0.03*s
print('net salary: ',s+a-d)


#Calculate net sales where net sales = gross sales – 10% discount of gross sales.
s=float(input('enter gross sales: '))
print('net sales=',s-(0.1*s))


#celcius into Fahrenheit
c=float(input('enter temperature in celcius: '))
print('temperature in farenheit: ',((9/5) * c) + 32)


#hrs to mins
h=int(input('enter hours to convert:'))
m=print('minutes=',h*60)


#mins to hrs 
m=int(input('enter minutes to convert:'))
print('hours=',m/60)


#divide 2 numbers
a=int(input("enter a number: "))
b=int(input("enter another number: "))
print("quotient=",a/b)



d=float(input('enter amount in dollars to convert to rupees'))
r=d*48
p=r/70
print(d,' dollars','=',p,' pounds')


#dollars to rupees
d=float(input('enter amount in dollars to convert to rupees'))
print(d,' dollers','=',d*48,' rupees')


#convert grams into kgs
g=float(input('enter weight in grams: '))
print("weight in kg: ",g/1000)


#kgs into grams
kg=float(input('enter weight in kg: '))
print('weight in grams: ',kg*1000)



#multiply 2 numbers
a=int(input("enter a number: "))
b=int(input("enter another number: "))
print("product=",a*b)


#rupee to dollar
r=float(input('enter amount in rupees to convert to dollars'))
print(r,' rupees','=',r/48,' dollars')


#subract 2 numbers
a=int(input("enter a number: "))
b=int(input("enter another number: "))
print("difference=",a-b)


#Swap two values
a=int(input('enter first no.: '))
b=int(input('enter second no.: '))
print('before swapping: ',a,b)
a,b=b,a
print('after swapping: ',a,b)