def count_alpha_digits(s):
    #Initialize dictionary to store count
    c = {"alphabets": 0, "digits": 0}

    for char in s:
        if char.isalpha():  #increment count if alfabate
            c["alphabets"] += 1
        elif char.isdigit():  #increment count if digit
            c["digits"] += 1

    return c

input_string = "MIIAAAOOOO 11!!!11!!"
count = count_alpha_digits(input_string)

print(f"Count of alphabets and digits: {count}")
