def q3():
    def count_vowels(s:str, index=0):
        if index == len(s):
            return 0
        if s[index].lower() in 'aeiou':
            return 1 + count_vowels(s, index + 1)
        else:
            return count_vowels(s, index + 1)
    s=input("Enter any string:")
    print("No of vowels:",count_vowels(s))
q3()