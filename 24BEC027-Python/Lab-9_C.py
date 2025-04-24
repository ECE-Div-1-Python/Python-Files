
def count_lower_upper():
    dict={}
    s=input("Enter a string:")
    a=0
    b=0
    for i in s:
        if(i.isupper()):
            a+=1
        else:
            b+=1
    dict["uppercase"]=a
    dict["lowercase"]=b
    print(dict)

def compute():
    n=input("Enter the number:")
    a=n
    b=n*2
    c=n*3
    d=n*4
    e=int(a)
    f=int(b)
    g=int(c)
    h=int(d)
    print(e+f+g+h)

def create_array(x, y, z, value):
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

array = create_array(3, 4, 5, 7)
for layer in array:
    print(layer)

def ls4():
    def sum_avg(a,b,c,d,e):
        Total=a+b+c+d+e
        Avg=a+b+c+d+e/5
        return Total,Avg
    a=int(input("Marks of first subject:"))
    b=int(input("Marks of second subject:"))
    c=int(input("Marks of third subject:"))
    d=int(input("Marks of forth subject:"))
    e=int(input("Marks of fifth subject:"))
    Total,Avg=sum_avg(a,b,c,d,e)
    print(f"Total={Total}")
    print(f"Avg={Avg}")

import string
def ls5():
    def ispangram(s):
        alphabet_set = set(string.ascii_lowercase)
        return alphabet_set <= set(s.lower())

    test_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Crazy Fredrick bought many very exquisite opal jewels"
    ]

    for sentence in test_sentences:
        print(f'"{sentence}" is a pangram: {ispangram(sentence)}')

    str = input("\nEnter the string : ")
    print(f'"{str}" is a pangram: {ispangram(str)}')

def ls6():
    def Lst_tup(x):
        lst=[]
        for i in range(1,x+1):
            lst.append((i,i**2,i**3))
        return lst
    n=int(input("Enter the end value:"))
    list=Lst_tup(n)
    print(list)

def ls7():
    def ispalindrome(str):
        str.lower()
        lst=list(str)
        for i in lst:
            if i == " ":
                lst.remove(i)
        print(lst)
        if lst == lst[::-1]:  
            print("Is a palindrome")
        else:
            print("Not a palindrome")
    str=input("Enter the string:")
    ispalindrome(str)

def convert(str):
    return " ".join(sorted(set(str.split())))
str=input("Enter the string:")
print(convert(str))

def ls9():
    def count_alpha_digits(str):
        count_alpha = 0
        count_digit = 0

        for element in str:
            if(65<=ord(element)<=90 or 97<=ord(element)<=122):
                count_alpha+=1

        for element in str:
            if(48<=ord(element)<=57):
                count_digit+=1
               
        print({"No. of alphabets in the string is" : count_alpha, "No. of digits in the string is" : count_digit})
    str = input("Enter the string : ")
    count_alpha_digits(str)

from collections import defaultdict
import string
def ls10():
    def frequency(input_string):

        translator = str.maketrans('', '', string.punctuation)
        cleaned_string = input_string.translate(translator)
        words = cleaned_string.split()

        word_freq = defaultdict(int)
        for word in words:
            word_freq[word] += 1
        sorted_words = sorted(word_freq.keys())
        sorted_freq = {word: word_freq[word] for word in sorted_words}
        return sorted_freq

    input_string = input("Enter the string : ")
    result = frequency(input_string)
    print(result)

def create_list():
    list1 = input("Enter the elements for list1 separated by space : ").split()
    list2 = input("Enter the elements for list2 separated by space : ").split()

    return list(set(list1) & set(list2))
print("Intersection of Two Lists :-",create_list()) 

def prime_factors(n, divisor=2):
    if n <= 1:
        return []
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    else:
        return prime_factors(n, divisor + 1)

num = int(input("Enter a positive integer: "))
if num > 0:
    print("Prime factors:", prime_factors(num))
else:
    print("Please enter a positive integer.")

def binary_equivalent(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binary_equivalent(n // 2) + str(n % 2)

num = int(input("Enter a positive integer: "))
if num >= 0:
    print("Binary equivalent:", binary_equivalent(num))
else:
    print("Please enter a non-negative integer.")

def count_vowels(s, index=0):
    vowels = "aeiouAEIOU"
    if index == len(s):
        return 0
    return (1 if s[index] in vowels else 0) + count_vowels(s, index + 1)

user_input = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(user_input)}")

def reverse_list(lst):
    if not lst:  
        return []
    return [lst[-1]] + reverse_list(lst[:-1]) 

numbers = input("Enter the elements for list1 separated by space : ").split()
print("Original List :-",numbers)
print("Reversed List :-",reverse_list(numbers))  

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))

result = power(a=a, b=b)
print(f"{a}^{b} = {result}")

def sanitize_list(lst, index=0):
    if index == len(lst):
        return
    if lst[index] < 0:
        lst[index] = 0
    sanitize_list(lst, index + 1)

lst = list(map(int, input("Enter list elements separated by space: ").split()))

sanitize_list(lst)
print("Sanitized list:", lst)

def average_recursive(lst, index=0, total=0):
    if index == len(lst):
        return total / len(lst) if len(lst) > 0 else 0
    return average_recursive(lst, index + 1, total + lst[index])

lst = list(map(int, input("Enter list elements separated by space: ").split()))

avg = average_recursive(lst)
print("Average of the list:", avg)

def string_length_recursive(s, index=0):
    if index == len(s):
        return index
    return string_length_recursive(s, index + 1)

s = input("Enter a string : ")
print("Length of the string:", string_length_recursive(s))

def fun():
    return "fun() exicuted."

def disp():
    return "disp() exicuted."
    
def msg():
    return "msg() exicuted."   

lst = [fun(), disp(), msg()]        

for l in lst:
    print(l)

def add_elements_of_lists():
    lst1 = [1,2,3,4,5,6]
    lst2 = [6,5,4,3,2,1]

    lst = list(map(lambda i, j : i + j, lst1, lst2))
    print(lst)

add_elements_of_lists()   

import random

def square_of_random_nums():
    lst = [random.randrange(-15,16) for _ in range(10)]
    print(f"Original List of Numbers : {lst}")
    lst = list(map(lambda x : x*x, lst))
    print(f"List of square of Numbers : {lst}")

square_of_random_nums()   

def check_palindrom():
    lst = ['madam','Python','malayalam',12321]
    lst = list(filter(lambda s: str(s) == str(s)[::-1], lst))
    print(lst)

check_palindrom() 

def name_char_check(lst):
    filtered_lst = list(filter(lambda s : len(s) > 8,lst))
    return filtered_lst

lst = input("Enter names of Faculty Members separated by space : ").split()
print(name_char_check(lst))
