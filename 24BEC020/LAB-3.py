def count_vowels():
    string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    print(count)

def to_lower_case():
    string = input("Enter a string: ")
    result = ""
    for char in string:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    print(result)

def to_upper_case():
    string = input("Enter a string: ")
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)

def toggle_case():
    string = input("Enter a string: ")
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    print(result)

def check_substring():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    if string2 in string1:
        print("Yes, the second string is present in the first string.")
    else:
        print("No, the second string is not present in the first string.")

def remove_substring():
    string1 = input("Enter the first string: ")
    remove_string = input("Enter the string to remove: ")
    result = ""
    i = 0
    while i < len(string1):
        if string1[i:i+len(remove_string)] == remove_string:
            i += len(remove_string)
        else:
            result += string1[i]
            i += 1
    print(result)
