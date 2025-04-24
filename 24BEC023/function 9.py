def count_alpha_digits(s):
    counts = {'alphabets': 0, 'digits': 0}

    for char in s:
        if char.isalpha():  
            counts['alphabets'] += 1
        elif char.isdigit(): 
            counts['digits'] += 1

    return counts

test_string = "Hello123, this is test456!"
result = count_alpha_digits(test_string)

print(f"Input String: {test_string}")
print(f"Alphabets Count: {result['alphabets']}")
print(f"Digits Count: {result['digits']}")
