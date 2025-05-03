a=int(input("Enter the value of a :"))
print(a)
b=int(input("Enter the value of b :"))
print(b)
c = a + b
print(c)


a=int(input("Enter the value of a :"))
print(a)
b=int(input("Enter the value of b :"))
print(b)
c = a - b
print(c)



a=int(input("Enter the value of a :"))
print(a)
b=int(input("Enter the value of b :"))
print(b)
c = a * b
print(c)



a=int(input("Enter the value of a :"))
print(a)
b=int(input("Enter the value of b :"))
print(b)
c = a / b
print(c)



a=int(input("Enter the value of a :"))
print(a)
b=int(input("Enter the value of b :"))
print(b)
c= a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)


h=int(input("Enter Some Hours :"))
m=h*60
print(m)


a=int(input("Enter dollars :"))
r=a*48
print(r)


a=int(input("Enter dollars :"))
r=a*48
print(r)


r=int(input("Enter Rs."))
d = r/48
print(d)


d=int(input("Enter Dollars : "))
r = d*48
pound=r/70
print(pound)


g=int(input("Enter Grams :"))
kg = g/1000
print(kg)


kg =int(input("Enter Kg :"))
g = kg*1000
print(g)


byte=int(input("Enter Bytes :"))
kb = byte*1024
print(kb)
mb = byte*1048576
print(mb)
gb = byte*1073741824
print(gb)


cel = int(input("Enter Celcius :"))
f=(9/5*cel)+32
print(f)


f=int(input("Enter Fahrenheit :"))
c=5/9*(f-32)
print(c)


p=int(input("Enter Principal amount :"))
r=int(input("Enter the annual interest rate :"))
n=int(input("Enter Number of periods :"))
i = p*r*n/100
print(i)


l=int(input("Enter the Length :"))
a=l**2
print(a)
p=4*l
print(p)


l=int(input("Enter the length : "))
b=int(input("Enter the bridth : "))
a = l * b
print(a)
p=2*l +2*b
print(p)


r=int(input("Enter the Radius of Circle :"))
a=3.14*r*r
print(a)


b=int(input("Enter the base :"))
h=int(input("Enter the height :"))
a=0.5*b*h
print(a)


g=int(input("Enter gross salary :"))
#allowance is 10%
#deduction is 3%
salary=g+0.1-0.03
print(salary)


s1=int(input("Enter the marks of sub 1 : "))
s2=int(input("Enter the marks of sub 2 : "))
s3=int(input("Enter the marks of sub 3 : "))
total = s1 + s2 + s3
avg = total/3
print(avg)


a = 4
b = 7
a,b = b,a
print("a = ",a)
print("b = ",b)





a=int(input("Enter value of a : "))
print(a)
b=int(input("Enter value of b : "))
print(b)
if(a>b):
 print("a is Largest and b is smallest ")
else:print(" b is Largest and a is smallest")


a=int(input("Enter value of a :"))
print(a)
b=int(input("Enter value of b :"))
print(b)
c=int(input("Enter value of c :"))
print(c)
if(a>b and a>c):
    print("a is Largest and b,c are smallest")
if(b>a and b>c):
    print("b is Largest and a,c are smallest")
if(c>a and c>b):
    print("c is Largest and a,b are smallest")
      
a=int(input("Enter value of a :"))
if(a%2==0):
    print("a is even")
else:print("a is odd")


a=int(input("Enter a Number:"))
if(a%10==0):
    print("A number is divisible by 10")
else:print("A number is not divisible by 10")


age=int(input("Enter The Age:"))
if(age<18):
    print("Minor")
else:print("Major")    


year=int(input("Enter a year :"))
if(year%4==0 and year%100!=0):
    print("It is a leap year")
else:
    print("It is not a leap year")


a=int(input("Enter The 1st angle of a triangle:"))
b=int(input("Enter The 2nd angle of a triangle:"))
c=int(input("Enter The 3rd angle of a triangle:"))
if(a+b+c==180):
    print("Triangle is valid")
else:print("Triangle is not valid")


year=int(input("Enter a year :"))
if(year%4==0 and year%100!=0):
    print("It is a leap year")
else:
    print("It is not a leap year")


length=int(input("Enter length of a rectangle : "))
breadth=int(input("Enter breadth of a rectangle : "))
area=length*breadth
perimeter=2*(length+breadth)
print("Area of rectangle is",area)
print("Perimeter of rectangle is",perimeter)
if(area>perimeter):
            print("Area of rectangle is greater than it's perimeter")
else:
    print("Area of rectangle is not greater than it's perimeter")



x1=int(input("Enter 1st x cocordinate X1:"))
y1=int(input("Enter 1st y cocordinate y1:"))
x2=int(input("Enter 2nd x cocordinate X2:"))
y2=int(input("Enter 2nd y cocordinate y2:"))
x3=int(input("Enter 3rd x cocordinate X3:"))
y3=int(input("Enter 3rd y cocordinate y3:"))
d1=((x2-x1)**2+(y2-y1)**2)**1/2
d2=((x3-x2)**2+(y3-y2)**2)**1/2
d3=((x3-x1)**2+(y3-y1)**2)**1/2
if d3==d1+d2:
    print("Given points are colinear")
else:
    print("Given points are not colinear")


x=int(input("Enter x-coordinte of center : "))
y=int(input("Enter y-coordinte of center : "))
a=int(input("Enter x-coordinte of point : "))
b=int(input("Enter y-coordinte of point : "))
radius=int(input("Enter Radius of circle : "))
distance =(((x-a)**2+(y-b)**2)**(1/2))
if(distance<radius):
    print("Point is inside of the circle")
if(distance==radius):
    print("Point is on the circle")
if(distance>radius):
    print("Point is outside of the circle")


a=int(input("Enter a number : "))#between 0 to 19

words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
             "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
             "Seventeen", "Eighteen", "Nineteen"]
if(a<20):
  print(words[a])
else:
    print("Invalid input")


sub1=int(input("Entere marks of sub 1 : "))
sub2=int(input("Entere marks of sub 2 : "))
sub3=int(input("Entere marks of sub 3 : "))
total = sub1+sub2+sub3
print("Total marks =",total)
Avg = total/3
print("Avg = ",Avg)
#if(sub1=Absent):
   # print("NA")
if(0<=sub1<=39):
    print("sub 1 = F")
if(40<=sub1<=44):
    print("sub 1 = P")
if(45<=sub1<=49):
    print("sub 1 = C")
if(50<=sub1<=54):
    print("sub 1 = B")
if(55<=sub1<=59):
    print("sub 1 = B+")
if(60<=sub1<=69):
    print("sub 1 = A")
if(70<=sub1<=79):
    print("sub 1 = A+")
if(80<=sub1<=100):
    print("sub 1 = O")
if(0<=sub2<=39):
    print("sub 2 = F")
if(40<=sub2<=44):
    print("sub 2 = P")
if(45<=sub2<=49):
    print("sub 2 = C")
if(50<=sub2<=54):
    print("sub 2 = B")
if(55<=sub2<=59):
    print("sub 2 = B+")
if(60<=sub2<=69):
    print("sub 2 = A")
if(70<=sub2<=79):
    print("sub 2 = A+")
if(80<=sub2<=100):
    print("sub 2 = O")
if(0<=sub3<=39):
    print("sub 3 = F")
if(40<=sub3<=44):
    print("sub 3 = P")
if(45<=sub3<=49):
    print("sub 3 = C")
if(50<=sub3<=54):
    print("sub 3 = B")
if(55<=sub3<=59):
    print("sub 3 = B+")
if(60<=sub3<=69):
    print("sub 3 = A")
if(70<=sub3<=79):
    print("sub 3 = A+")
if(80<=sub3<=100):
    print("sub 3 = O")








def vowel(n):
    count=0
    for b in n:
        if(b=='a' or b=='e' or b=='i' or b=='o' or b=='u' or b=='A' or b=='E' or b=='I' or b=='O' or b=='U'):
            count+=1
    return count
str=input("Enter a string : ")
print("Number of vowels  : ",vowel(str)) 
            



   
def lowercase(string):
    str1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str2='abcdefghijklmnopqrstuvwxyz'
    new
    for i in range(len(string)):
        for j in range(len(str1)):
            if(str[j]==str[i]):
                new+=str2[j]
            elif str[j]==string[i]:
                new+=string[i]
    print(new)
string=input("Enter the string : ")
lowercase(string)



def to_lower_case(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            # Convert uppercase letter to lowercase
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def to_upper_case(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            # Convert lowercase letter to uppercase
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def toggle_case(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            # Convert lowercase letter to uppercase
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            # Convert uppercase letter to lowercase
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

# Test the functions
string = input('Enter a string: ')
print("Lower Case:", to_lower_case(string))
print("Upper Case:", to_upper_case(string))
print("Toggle Case:", toggle_case(string))



string1="hello world"
substring="world"
if substring in string1:
    print("true")
else:
    print("false")



input_string="hello world"
vowels='aeiouAEIOU'
consonants='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
vowel_count=0
consonants_count=0
for char in input_string:
    if char in vowels:
        vowel_count+=1
    elif char in consonants:
        consonants_count+=1
print(f"vowels:{vowel_count}")
print(f"consonants:{consonants_count}")




def find(s1,s2):
    if s1 in s2:
        return f"'{s1}' is present in '{s2}'"
    elif s2 in s1:
        return f"'{s2}' is present in '{s1}'"
    else:
        return "no string is present in another"
s1=input("Enter first string: ")
s2=input("Enter second string: ")
print(find(s1,s2))



def remove_substring(onestring, removestring):
    result = ''
    i = 0
    while i < len(onestring):
        if onestring[i:i+len(removestring)] == removestring:
            i += len(removestring)  
        else:
            result += onestring[i]  
            i += 1
    return result

onestring = "abcdef"
removestring = "cd"
finalstring = remove_substring(onestring, removestring)
print("Original String:", onestring)
print("String to Remove:", removestring)
print("Final String:", finalstring)
















import random
o=[]
for i in range(5):
    o.append(random.randrange(1,10))

            print(o)
l=[]
l1=[]
for x in range(5):
    b=input("Enter string:")
    l.append(b)
for x in l:
    y=x.upper()
    l1.append(y)
print('The original list =',l)
print('The upper case list =',l1)



l=[]
l1=[]
a=int(input("How many elements you want to enter:"))
for x in range(a):
    k=int(input("Enter temperature value in farenheit:"))
    c=5*(k-32)/9
    l.append(k)
    l1.append(c)
print("The farenheit list =",l)
print("The celsius list =",l1)


import random
l=[]
l1=[]
n=0
while(n<5):
    k=random.randint(1,100)
    if(k%2==1):
        l.append(k)
        n+=1
print("The random odd number list =",l)
n=0
while(n<4):
    k=random.randint(1,100)
    if(k%2==0):
        l1.append(k)
        n+=1
print("The random even number list =",l1)
l.insert(2,l1)
l.pop(3)
print("The 3rd list =",l)

l2=[]
for x in l:
    print(x)
    l2.extend([x])
print("The flatterned list =",l2)
l2.sort()
print("The sorted listed =",l2)


l=[]
n=int(input("Enter n number of elements :  ")) 
for i in range(0,n):
   i=input()
   l.append(i)
print("list elements are : ",l)


import random
l=[]
n=0
while(n<20):
    l.append(random.randint(1,20))
    n+=1
print("list is =",l)
a=int(input("Enter a number:"))
m=0
for y in l:
    if(y==a):
        print("One of the position is =",m)
    m+=1


import random 
l1=[]
l2=[]
for x in range(10):
    k=random.randint(1,25)
    l1.append(k)
for y in range(10):
    k=random.randint(1,25)
    l2.append(k)
l3=[i for i in l1 if i not in l2]
print("The first list is :",l1)
print("The second list is :",l2)
print("The modified list is :",l3)


import random
l=[]
for i in range(5):
    l.append(random.randint(80,100))
print(l)



import random
l=[]
n=0
while(n<10):
    k=random.randint(1,20)
    l.append(k)
    n+=1
print("Original=",l)
l1=[]
for x in range(0,len(l)):
    for y in range(x+1,len(l)):
        if(l[x]==l[y]):
            break
    else:
        l1.append(l[x])
print("The non duplicate list =",l1)
            
            
import random 
l1=[]
l2=[]
for x in range(10):
    k=random.randint(1,25)
    l1.append(k)
for y in range(10):
    k=random.randint(1,25)
    l2.append(k)
l3=[i for i in l1 if i not in l2]
print("The first list is :",l1)
print("The second list is :",l2)
print("The modified list is :",l3)


import random
l=[]
l1=[]
l2=[]
for x in range(0,30):
    k=random.randint(-50,50)
    l.append(k)
    if(k>=0):
        l1.append(k)
    else:
        l2.append(k)
print("The main list =",l)
print("The positive list =",l1)
print("The negative list =",l2)








for hour in range(0,24):
    if(hour==0):
        print("12 Midnight")
    elif(hour<12):
        print(f"{hour}AM")
    elif(hour==12):
        print("12 Noon")
    else :
        print(f"{hour-12}PM")
        
import math
degree=int(input("Enter an angle in degree : "))
x=degree*math.pi/180
sin(x)==0
term=0
for i in range(term):
    power=2*i+1
    term=((-1)**i)*(x**power)/math.factorial(power)
sin(x)==sin(x)+term
printf("Value of sin(x) is : ",sin(x))


num=int(input("Enter the Number : "))
fact=i=1
while(i<=num):
    fact=fact*i
    i=i+1
print("Factorial of given number is : ",fact)


n=int(input("Enter a number for get elements of Fibonacci series: "))
a=0
print(a)
b=1
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a,b=b,c
    

a=int(input("Ënter a number :"))
for i in range(1,11):
 b=a*i
 print(b)


n=int(input("Enter the value of N : "))
for i in range(n,0,-1):
      print(i)


n=int(input("Enter value for n : "))
r=int(input("Enetr value for r : "))
fact=i=1
while(i<=n):
    fact=fact*i
    i = i+1
numerator = fact
sub=n-r
fact=fact*i
i=i+1
while(i<=sub):
    fact=fact*i
    i=i+1
denominator=fact
fact=i=1
while(i<=r):
    fact=fact*i
    i=i+1
denominator=denominator*fact
comb=numerator/denominator
print("\n nCr = ",comb)



n=int(input("Enter the value of n : "))
r=int(input("Enter the value of r : "))

fact=i=1
while(i<=n):
    fact=fact*i
    i=i+1
numerator = fact
sub = n-r

fact=i=1
while(i<=sub):
    fact=fact*i
    i=i+1
denominator=fact
perm=numerator/denominator
print("nPr is : ",perm)



a=int(input("Enter a number : "))
for i in range(1,a+1):
    if(i*i==a):
        print("Ä number is perfact")
        break
else:
    print("A number is not perfact")




a=int(input("Enter a number : "))
for i in range(1,a+1):
    if(i*i==a):
        print("Ä number is perfact")
        break
else:
    print("A number is not perfact")



triplets=[]
for a in range(1,20):
    for b in range(a,20):
        for c in range(b,20):
            if(a**2+b**2==c**2):
                triplets.append((a,b,c))
print(triplets)




import operator
Employee_Record=[(1,'Driti',48,'HR',19000),(2,'Rasmit',52,'HR', 22000),(3,'Krishiv',29,'HEAD',150000)]
#Filter employee by Department
dept='HR'
Filter_employee = [emp[1] for emp in Employee_Record if emp[3]==dept]
print("�mployees names that are in 'HR' department : ",Filter_employee)
#sort employee by Salary

salary=sorted(Employee_Record,key=operator.itemgetter(4))
print("Employees names acorrding to their salary",salary)
print("Employe name  with Highest salary: ",salary[len(salary)-1])


import datetime
date1=(30,4,2007)
date2=(30,4,2025)
d1=datetime.datetime(date1[2],date1[1],date1[0])
d2=datetime.datetime(date2[2],date2[1],date2[0])
days=abs((d2-d1).days)
print("Days between two dates : ",days)


tuple=(15,30,4,2007)
print("Original tuple : ",tuple)
tuple=(tuple[1],tuple[2],tuple[3])
print("Modified tuple: ",tuple)


tuple=(30,4,2008)
print("Original tuple : ",tuple)
tuple=(tuple[0],tuple[1],2007)
print("Modified tuple : ",tuple)


l=['G1','G2',('B1','B2'),'G3']
print(l)
boys=0
girls=0
for ele in l:
    if isinstance(ele,tuple):
        boys+=len(ele)
    else:
        girls+=1
print("The number of Boys : ",boys)
print("The number of Girls : ",girls)



tuple_lst=[(1,2),(),(30,4),(),(1,5)]
print("List : ",tuple_lst)
List=[t for t in tuple_lst if t]
print("List without empty list : ",List)


l=[(1,"Richa",17),(2,"Reni",17),(3,"Riya",18)]
print(l)
rollNumbers=[]
name=[]
age=[]
for student in l:
    rollNumbers.append(student[0])
    name.append(student[1])
    age.append(student[2])
print("Roll Numbers : ",rollNumbers)
print("Names : ",name)
print("Age : ",age)


food_items=[("Burger",449),("Pizza",759),("Sizzelers",889)]
sorted_Fooditems=sorted(food_items,key=operator.itemgetter(1),reverse=True)
print("Sorted food items : ",sorted_Fooditems)




#Taking input for first dictionary
dict1 = {}
n1 = int(input("Enter the number of elements for first dictionary: "))
for i in range(n1):
    key = input("Enter key for dict1: ")
    value = int(input("Enter value for dict1: "))
    dict1[key] = value

# Taking input for second dictionary
dict2 = {}
n2 = int(input("Enter the number of elements for second dictionary: "))
for i in range(n2):
    key = input("Enter key for dict2: ")
    value = int(input("Enter value for dict2: "))
    dict2[key] = value
    
# Taking input for third dictionary
dict3 = {}
n3 = int(input("Enter the number of elements for third dictionary: "))
for i in range(n3):
    key = input("Enter key for dict3: ")
    value = int(input("Enter value for dict3: "))
    dict3[key] = value


# Manually merging dictionaries
merged_dict = {}

# Adding elements of dict1 to merged_dict
for key in dict1:
    merged_dict[key] = dict1[key]

# Adding elements of dict2 to merged_dict
for key in dict2:
    merged_dict[key] = dict2[key]

# Adding elements of dict3 to merged_dict
for key in dict3:
    merged_dict[key] = dict3[key]


# Printing the merged dictionary
print("Merged 4th Dictionary is :", merged_dict)





dict1 = {}
n = int(input("Enter the number of elements for the dictionary: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

# Manually sorting dictionary using Selection Sort
items = list(dict1.items())  # Convert dictionary to list of tuples

for i in range(len(items)):
    min_index = i
    for j in range(i + 1, len(items)):
        if items[j][1] < items[min_index][1]:  # Comparing values
            min_index = j
    
    items[i], items[min_index] = items[min_index], items[i]


sorted_dict = {}
for item in items:
    sorted_dict[item[0]] = item[1]

print("Sorted Dictionary:", sorted_dict)




def create_square_dict():
    num_keys = int(input("Enter the number of keys: "))
    square_dict = {}

    for i in range(num_keys):
        key = int(input(f"Enter key {i+1}: "))
        square_dict[key] = key ** 2

    print("\nSquare Dictionary:")
    for key, value in square_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    create_square_dict()



print("Name: Vatsal Bhavsar")
print("Rollno.: 24BEE125")
# Taking input for the dictionary
dict1 = {}
n = int(input("Enter the number of elements for the dictionary: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

# Finding max and min values manually
values = list(dict1.values())  # Extract values from dictionary

# Initializing max and min with the first value
max_value = values[0]
min_value = values[0]

# Iterating through values to find max and min
for val in values:
    if val > max_value:
        max_value = val
    if val < min_value:
        min_value = val

# Printing the results
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)



string = input("Enter a string: ")
char_frequency = {}

for char in string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Character Frequency:", char_frequency)










import random

# Generate a set of 10 random numbers between 15 and 45
random_numbers = {random.randint(15, 45) for _ in range(10)}

# Count numbers less than 30
count_less_than_30 = sum(1 for num in random_numbers if num < 30)

# Remove numbers greater than 35
random_numbers = {num for num in random_numbers if num <= 35}

print("Generated Set:", random_numbers)
print("Count of numbers that are less than 30 in set :", count_less_than_30)




words = ["apple", "banana", "cherry", "date", "elderberry"]
uppercase_set = {word.upper() for word in words}
print("Uppercase Set:", uppercase_set)



names ={"Alice", "Bob", "Charlie", "David", "Emma"}
names_set ={"Alice", "Bob", "Charlie", "David", "Emma"}

names_set.discard("Charlie")
names_set.add("Carlos")

names_set.discard("Alice")
names_set.discard("David")
print("The Original Set is : ",names)
print("Final Set of Names:", names_set)



names = {"Alice", "Aaron", "Andrew", "Brian", "Bella", "Ben"}


set_A = {name for name in names if name.startswith("A")}
set_B = {name for name in names if name.startswith("B")}
print("The original set is : ",names)
print("Names starting with A:", set_A)
print("Names starting with B:", set_B)










def array(a,b,c,value):
    array=[[value for i in range(c)for i in range(b)for i in range(a)]]
    return array
x=int(input("Enter Number of raws: "))
y=int(input("Enter Number of columns: "))
z=int(input("Enter vv : "))
values=int(input("Enter Values: "))
print(array(x,y,z,values))


def count_upper_lower(str):
    uppercase=0
    lowercase=0
    for ch in str:
        if ch.isupper():
            uppercase+=1
        elif ch.islower():
            lowercase+=1
    return {"Uppercase":uppercase,"Lowercase":lowercase}

sample_str=input("Enter a string : ")
result=count_upper_lower(sample_str)
print("Number of character : ",result)


def compute(n):
    n1=int(str(n))
    n2=int(str(n)*2)
    n3=int(str(n)*3)
    n4=int(str(n)*4)

    return n1+n2+n3+n4
for i in range(4,8):
    print(f"compute({i})= ",compute(i))



def sum_avg(r,s,t,u,v):
    sum=0
    avg=0
    sum=r+s+t+u+v
    avg=sum/5
    return sum,avg
print(sum_avg(1+3+5+8+9))



print("Name: Rutva Mehta")
print("Rollno.: 24BEE122")

# Define file names
input_file = "input.txt"
output_file = "cleaned_text.txt"

# Open the input file and read lines
with open(input_file, "r") as file:
    lines = file.readlines()

# List of words to remove
remove_words = ["a", "an", "the"]

# Process each line
with open(output_file, "w") as file:
    for line in lines:
        words = line.split()  # Split line into words
        new_words = [word for word in words if word.lower() not in remove_words]  # Remove unwanted words
        file.write(" ".join(new_words) + "\n")  # Write cleaned line

print(f"File '{output_file}' created successfully with words removed.")


import os

source_file = "source_folder/example.txt"
destination_dir = "destination_folder/new_subdir"
destination_file = os.path.join(destination_dir, "example.txt")

os.makedirs(destination_dir, exist_ok=True)

with open(source_file, "rb") as src:
    content = src.read()

with open(destination_file, "wb") as dst:
    dst.write(content)

print(f"Copied '{source_file}' to '{destination_file}' successfully.")



import csv

# Data to write
students = [
    ["Roll No", "Name", "Subject1", "Subject2", "Subject3"],
    [101, "Alice", 85, 90, 80],
    [102, "Bob", 75, 85, 95],
    [103, "Charlie", 90, 92, 88]
]

# Writing to CSV
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully.")
f=open('students.csv','w')






name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""

with open("contact.vcf", "w") as file:
    file.write(vcard_content)

print("vCard created successfully.")



source_file = "input.txt"
destination_file = "output.txt"

with open(source_file, "r") as src, open(destination_file, "w") as dest:
    for line in src:
        dest.write(line.upper())

print("File copied with content converted to uppercase into another.")





def merge_files_alternatively(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
     
        len1, len2 = len(lines1), len(lines2)
        
       
        for i in range(max(len1, len2)):
            if i < len1:
                out.write(lines1[i])
            if i < len2:
                out.write(lines2[i])

merge_files_alternatively('file1.txt', 'file2.txt', 'merged_output.txt')




import csv

# Data to write
students = [
    ["Roll No", "Name", "Subject1", "Subject2", "Subject3"],
    [101, "Alice", 85, 90, 80],
    [102, "Bob", 75, 85, 95],
    [103, "Charlie", 90, 92, 88]
]

# Writing to CSV
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully.")
































