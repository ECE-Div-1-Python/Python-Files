
user_input = input("Enter a string: ")
alpha =0
digit=0
for character in str:
    if character.isalpha():
            alpha += 1
    elif character.isdigit():
            digit += 1
print(f"number of digit is:",digit)   
print(f"number of alpha: ",alpha)


