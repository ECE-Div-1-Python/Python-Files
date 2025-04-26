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
