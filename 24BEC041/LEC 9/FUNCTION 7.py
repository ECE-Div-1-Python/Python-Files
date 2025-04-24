def is_palindrome(n):
    s=s.lower()
    s=list(n)
    b=s.copy()
    s.reverse()
    if b==s:
        print("It is palindrome")
    else:
        print("It is not palindrome")
is_palindrome(input("enter the word:"))