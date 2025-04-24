#1.	Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos. Replace the third element of odd integers with  a list of 4 even integers. Flattern, sort and print the list. Provide appropriate message at each 
import random
def list_():
    l1=[random.randint(1,200)*2-1 for a in range(5)]
    l2=[random.randint(1,200)*2 for a in range(4)]
    print("List of 5 random odd integers:",l1)
    print("List of 5 random even integers:",l2)
    l1.pop(2)
    print(l1,l2)
    l1.insert(2,l2)
    print(l1)
    l3=[]
    for x in l1:
        l3.extend(x) if isinstance(x,list) else l3.append(x)
    print(l3)    
list_()     

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#2.	Generate 20 random integers and store them in a list. Accept a number from the user and print position of all occurrences of that number in the list.
import random
def list():
    l1=[random.randint(1,200)*2 for _ in range(20)]
    print(l1)
    i=int(input("Enter a number:"))
    if i in l1:
        s=[index for index,x in enumerate(l1) if x==i]
        print(i, "is found at positions:", s)
    else:
        print(i, "is not found in the list.")

list()

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#3.	Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.
import random
def number():
    l1=[random.randint(1,30) for a in range(50)]
    unique_no=[]
    for i in l1:
        if i not in unique_no:
            unique_no.append(i)
    unique_no.sort()        
    print(unique_no)
number()

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#4.	Generate 30 random numbers and put them in a list. Create two more lists – one containing only +ve numbers and another with –ve nos.
import random
def positve_negative():
    l1=[random.randint(-100,100) for a in range(30)]
    print(l1)
    l2=[]
    l3=[]
    for a in l1:
        if a>0:
            l2.append(a)
        elif a<0:
            l3.append(a)
    print(f"Positive numbers:{l2}")
    print(f"negative numbers:{l3}")
    
positve_negative()

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#5.	A list contains 5 strings. Convert all these strings to uppercase
def str():
    str1=["apple","orange","grapes","watermelon","Pineapple"]
    upper_str1=[]
    for a in str1:
        upper_str1.append(a.upper())
    print(upper_str1)
str()

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#6.	Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.
def fahrenheit_to_celsius(f_temps):
    return [(f - 32) * 5 / 9 for f in f_temps]

fahrenheit_temps = [32, 68, 104, 212]
celsius_temps = fahrenheit_to_celsius(fahrenheit_temps)
print(celsius_temps)

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#9.	Take two lists of numbers. Create third list of numbers for only those numbers from first list which are not there in 2nd list (use list comprehension). 
def difference_list(list1, list2):
    return [num for num in list1 if num not in list2]

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

list3 = difference_list(list1, list2)

print(list3)
