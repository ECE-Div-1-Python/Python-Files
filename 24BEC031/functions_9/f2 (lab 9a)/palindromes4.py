lst = ['madam', 'Python', 'malayalam', 12321]
def is_palindrome(str):
    return str == str[::-1]

print("Palindrome strings in the list:")

for item in lst:
        if is_palindrome(item):
            print(item)