def string_length(s):
    if not s:
        return 0
    return 1 + string_length(s[1:])
print(string_length(input("enter the string: ")))