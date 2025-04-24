#1.	If a positive integer is entered through the keyword, write a recursive function to obtain the prime factors of the number
def prime(n,i=2):
    if n==1:
        return[]
    if n%i==0:
        return [i]+prime(n//i,i)
    else:
        return prime(n,i+1)
    
num=int(input("Enter a integer:"))
if num >0:
    factors=prime(num)
    print("Prime number:",factors)
else:
    print("Please enter a number greater than 0")

#2.	A positive integer is entered through the keyboard. Write a function to find its binary equivalent of this number
def dec_to_bin(n):
    # Base case: if n is 0, return empty string
    if n == 0:
        return ''
    else:
        return dec_to_bin(n // 2) + str(n % 2)
n = int(input("Enter an integer: "))
if n == 0:
    print("Binary equivalent: 0")
else:
    print("Binary equivalent:", dec_to_bin(n))

#3.	A string is entered through the keyboard. Write a recursive function that counts the number of vowels in this string.
def count_vowels(s, index=0):
    if index == len(s):
        return 0
    current_char = s[index].lower()
    if current_char in "aeiou":
        return 1 + count_vowels(s, index + 1)
    else:
        return count_vowels(s, index + 1)
t = input("Enter a string: ")
vowel_count = count_vowels(t)
print("Number of vowels:", vowel_count)

#4.	Write a recursive function that reverses the list of numbers that it receives.
def reverse(lst):
    if lst==[]:
        return []
    return [lst.pop()]+reverse(lst)
numbers=[4,5,3,7,9,1]
print(reverse(numbers))

#5.	Calculate ab where a and b received through the keyword using recursion.
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))
result = power(a, b)
print(f"{a} raised to the power {b} is: {result}")

#6.	A list contains some negative and some positive values. Write a recursive function that sanitizes the list by replacing all negative numbers with 0.
def sanitize_list(lst, index=0):
    if index == len(lst):
        return
    if lst[index] < 0:
        lst[index] = 0
    sanitize_list(lst, index + 1)
numbers = [5, -3, 8, -1, 0, -9, 7]
print("Original list:", numbers)
sanitize_list(numbers)
print("Sanitized list:", numbers)

#7.	Write a recursive function to obtain average of all numbers present in a given list.
def recursive_sum(lst, index=0):
    if index == len(lst):
        return 0
    else:
        return lst[index] + recursive_sum(lst, index + 1)
def recursive_average(lst):
    if len(lst) == 0:
        return 0  # avoid division by zero
    total = recursive_sum(lst)
    return total / len(lst)
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)
print("Average:", recursive_average(numbers))

#8.	Write a recursive function to obtain length of a given string.
def string_length(s):
    if s == "":
        return 0
    else:
        return 1 + string_length(s[1:])  
user_input = input("Enter a string: ")
length = string_length(user_input)
print("Length of the string:", length)
