
#Taking input for first dictionary
dict1 = {}
n1 = int(input("Enter the number of elements for first dictionary: "))
for i in range(n1):
    key = input("Enter key for dict1: ")
    value = int(input("Enter value for dict1: "))
    dict1[key] = value

# Taking input for second dictionary
dict2 = {}
n2 = int(input("Enter the number of elements for second dictionary: "))
for i in range(n2):
    key = input("Enter key for dict2: ")
    value = int(input("Enter value for dict2: "))
    dict2[key] = value
    
# Taking input for third dictionary
dict3 = {}
n3 = int(input("Enter the number of elements for third dictionary: "))
for i in range(n3):
    key = input("Enter key for dict3: ")
    value = int(input("Enter value for dict3: "))
    dict3[key] = value


# Manually merging dictionaries
merged_dict = {}

# Adding elements of dict1 to merged_dict
for key in dict1:
    merged_dict[key] = dict1[key]

# Adding elements of dict2 to merged_dict
for key in dict2:
    merged_dict[key] = dict2[key]

# Adding elements of dict3 to merged_dict
for key in dict3:
    merged_dict[key] = dict3[key]


# Printing the merged dictionary
print("Merged 4th Dictionary is :", merged_dict)





dict1 = {}
n = int(input("Enter the number of elements for the dictionary: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

# Manually sorting dictionary using Selection Sort
items = list(dict1.items())  # Convert dictionary to list of tuples

for i in range(len(items)):
    min_index = i
    for j in range(i + 1, len(items)):
        if items[j][1] < items[min_index][1]:  # Comparing values
            min_index = j
    
    items[i], items[min_index] = items[min_index], items[i]


sorted_dict = {}
for item in items:
    sorted_dict[item[0]] = item[1]

print("Sorted Dictionary:", sorted_dict)




def create_square_dict():
    num_keys = int(input("Enter the number of keys: "))
    square_dict = {}

    for i in range(num_keys):
        key = int(input(f"Enter key {i+1}: "))
        square_dict[key] = key ** 2

    print("\nSquare Dictionary:")
    for key, value in square_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    create_square_dict()



print("Name: Vatsal Bhavsar")
print("Rollno.: 24BEE125")
# Taking input for the dictionary
dict1 = {}
n = int(input("Enter the number of elements for the dictionary: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

# Finding max and min values manually
values = list(dict1.values())  # Extract values from dictionary

# Initializing max and min with the first value
max_value = values[0]
min_value = values[0]

# Iterating through values to find max and min
for val in values:
    if val > max_value:
        max_value = val
    if val < min_value:
        min_value = val

# Printing the results
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)



string = input("Enter a string: ")
char_frequency = {}

for char in string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Character Frequency:", char_frequency)
