1)
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

user_str = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_str))

2)

def to_lower(s):
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

def to_upper(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result

def toggle_case(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

test_str = input("Enter a string to change case: ")
print("Lower case:", to_lower(test_str))
print("Upper case:", to_upper(test_str))
print("Toggle case:", toggle_case(test_str))

3)

def is_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    for i in range(len1 - len2 + 1):
        match = True
        for j in range(len2):
            if str1[i + j] != str2[j]:
                match = False
                break
        if match:
            return True
    return False


main_str = input("Enter the main string: ")
search_str = input("Enter the string to search: ")

if is_substring(main_str, search_str):
    print("Yes, the second string is in the first string.")
else:
    print("No, the second string is not in the first string.")

4)

def remove_substring(main_str, remove_str):
    len_main = len(main_str)
    len_remove = len(remove_str)
    
    i = 0
    while i <= len_main - len_remove:
        if main_str[i:i+len_remove] == remove_str:
            return main_str[:i] + main_str[i+len_remove:]
        i += 1
    return main_str

main_string = input("Enter the main string: ")
remove_string = input("Enter the string to remove: ")

print("Final string:", remove_substring(main_string, remove_string))

