def frequency(s):
    words = s.split()
    freq_dict = {}
    
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    sorted_freq_dict = dict(sorted(freq_dict.items()))
    
    return sorted_freq_dict

test_string = "apple banana apple orange banana mango grape apple"
result = frequency(test_string)

print(f"Input String: {test_string}")
print("Word Frequencies (Sorted):")
for word, count in result.items():
    print(f"{word}: {count}")
