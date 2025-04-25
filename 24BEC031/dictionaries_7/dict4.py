# Read input string from the user
input_string = input("Enter a string: ")

# Dictionary to store character frequencies
char_frequency = {}

# Count frequency of each character
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Output the character frequency dictionary
print("Character Frequency Dictionary:", char_frequency)
