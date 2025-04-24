# 1. Count lowercase and uppercase letters in a string and return them as a dictionary
def count_lower_upper(s):
    result = {"lowercase": 0, "uppercase": 0}
    for char in s:
        if char.islower():
            result["lowercase"] += 1
        elif char.isupper():
            result["uppercase"] += 1
    return result

# Test the function
print(count_lower_upper("Hello World"))

# 2. Compute n + nn + nnn + nnnn for a given digit n
def compute(n):
    n = str(n)
    return int(n) + int(n*2) + int(n*3) + int(n*4)

# Test the function for digits 4 to 7
for i in range(4, 8):
    print(f"Result for {i}: {compute(i)}")

# 3. Create a 3D array with given dimensions and initialize values
def create_array(dim1, dim2, dim3, value):
    return [[[value for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

# Test the function
print(create_array(2, 3, 4, 5))

# 4. Calculate total and average of five subjects' marks
def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

# Test the function
marks = [85, 90, 78, 92, 88]
total, avg = sum_avg(marks)
print(f"Total: {total}, Average: {avg}")

# 5. Check if a string is a pangram (uses every letter of the alphabet)
def ispangram(s):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    s = s.lower()
    return set(s) >= alphaset

# Test the function with a pangram
print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("Crazy Fredrick bought many very exquisite opal jewels"))

# 6. Create a list containing tuples (x, x^2, x^3) for all x between 1 and n
def create_tuples(n):
    return [(x, x**2, x**3) for x in range(1, n+1)]

# Test the function
print(create_tuples(5))

# 7. Check if a string is a palindrome
def ispalindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Test the function
print(ispalindrome("A man a plan a canal Panama"))
print(ispalindrome("hello"))

# 8. Remove duplicate words and sort them alphanumerically
def convert(s):
    words = s.split()
    unique_words = sorted(set(words))
    return " ".join(unique_words)

# Test the function
print(convert("hello hello world this is a test test world"))

# 9. Count alphabets and digits in a string
def count_alpha_digits(s):
    result = {"alphabets": 0, "digits": 0}
    for char in s:
        if char.isalpha():
            result["alphabets"] += 1
        elif char.isdigit():
            result["digits"] += 1
    return result

# Test the function
print(count_alpha_digits("abc123"))

# 10. Compute frequency of words in a string and return sorted order
def frequency(s):
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items()))

# Test the function
print(frequency("hello world hello"))

# 11. Create a list containing the intersection of two lists
def create_list(list1, list2):
    return list(set(list1) & set(list2))

# Test the function
print(create_list([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
