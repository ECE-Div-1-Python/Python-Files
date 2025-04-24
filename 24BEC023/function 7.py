def ispalindrome(s):
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

test_string1 = "A man a plan a canal Panama"
test_string2 = "racecar"
test_string3 = "Hello World"

print(f"Is palindrome? '{test_string1}' -> {ispalindrome(test_string1)}")
print(f"Is palindrome? '{test_string2}' -> {ispalindrome(test_string2)}")
print(f"Is palindrome? '{test_string3}' -> {ispalindrome(test_string3)}")
