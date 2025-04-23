def count_alpha_digits(str):
    count_digit = 0
    count_alpha = 0
    for i in str:
        y = ord(i)
        if((y<=122 and y>=97) or (y<=90 and y>=65)):
            count_alpha += 1
        if(y<=57 and y>=48):
            count_digit += 1
    print("No. of digits in string : ", count_digit)
    print("No. of alpha in string : ", count_alpha)
str = input("Enter a string : ")
count_alpha_digits(str)