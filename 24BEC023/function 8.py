def convert(s):
    unique_sorted_words = sorted(set(s.split()))
    return ' '.join(unique_sorted_words)

test_string = "apple banana apple orange banana mango grape"
result = convert(test_string)

print(f"Original String: {test_string}")
print(f"Processed String: {result}")
