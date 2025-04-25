def ch_frequency(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
string1=input("enter the string: ")
frequency = ch_frequency(string1)
print(frequency)

