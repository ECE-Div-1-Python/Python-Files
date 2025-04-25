input_string=input("enter the text :")
result = ""
for char in input_string:
        # Check if the character is uppercase (ASCII value between 65 and 90)
        if 65 <= ord(char) <= 90:
            # Convert to lowercase by adding 32 to the ASCII value
            result += chr(ord(char) + 32)
        else:
            result += char 
print(result) 
