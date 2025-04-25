def ispalindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()

    #reverse string and check
    if s == s[::-1]:
        return True
    else:
        return False
    
s1 = "A man a plan a canal Panama"
if ispalindrome(s1):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")