#1.	Define three functions fun(), disp() and msg(). Store them in a list and call them one by one in a loop.
def fun():
    print("Function")
def disp():
    print("Display")
def msg():
    print("Message")
functions=[fun,disp,msg]
for i in functions:
    i() 
"***************************************************************************************************************"
#2.	Suppose there are two lists, one containing numbers from 1 to 6, and other containing numbers from 6 to 1. Write a program to obtain a list that contains elements obtained by adding 
def adding(a,b):
    c=[a[i] + b[i] for i in range(len(a))]
    return c
a=[1,2,3,4,5,6]
b=[6,5,4,3,2,1]
print(adding(a,b))
"***************************************************************************************************************"
#3.	Generate the list of 10 different random numbers between -15 and 15. Create a new list by obtaining square of all numbers in a list.
import random
def sorted_number():
    list=[random.randint(-15,16) for i in range(10)]
    list=sorted(set(list))
    print(list)
sorted_number()
"***************************************************************************************************************"
#4.	Consider the following list:
#lst = ['madam','Python',"malayalam",12321]
#Write a program to print those strings which are palindromes
def palindrome(s):
    s=str(s)
    return s==s[::-1]
lst = ['madam','Python',"malayalam",12321]
print("palindrome in the list:")
for item in list:
    if palindrome(item):
        print(item)
"***************************************************************************************************************"
#5.	A list contains names of Faculty Members.
#  Write a program to filter out those names whose length is more than 8 characters.
def filter_faculty_names(faculty_names):
    filtered_names = [i for i in faculty_names if len(i) > 8]
    return  filtered_names
faculty_list = ["Dr. Smith", "Professor Williams", "Mr. Johnson", "Associate Professor Davis", "Ms. Lee", "Dr. Brown", "Vice Chancellor Sharma"]
long_names = filter_faculty_names(faculty_list)
print("Faculty names with more than 8 characters:")
for name in long_names:
  print(name) 
