def count_lower_upper(s):
    counts = {'lowercase': 0, 'uppercase': 0}

    for char in s:
        if char.islower():
            counts['lowercase'] += 1
        elif char.isupper():
            counts['uppercase'] += 1

    return counts

string = "Hello World This is a Test String ."
result = count_lower_upper(string)

print(f"Input String: {string}")
print(f"Lowercase Letters: {result['lowercase']}")
print(f"Uppercase Letters: {result['uppercase']}")
