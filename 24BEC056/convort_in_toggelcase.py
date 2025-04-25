input_string=input("enter the string :")
result = ""
for char in input_string:
        # Check if the character is lowercase
        if 97 <= ord(char) <= 122:
            # Convert to uppercase
            result += chr(ord(char) - 32)
        # Check if the character is uppercase
        elif 65 <= ord(char) <= 90:
            # Convert to lowercase
            result += chr(ord(char) + 32)
        else:
            result += char
print(result)