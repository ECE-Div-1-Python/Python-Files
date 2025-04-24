def vowel_occurence(str):
    b = ['A','E','I','O','U','a','e','i','o','u']
    count = 0
    for i in str:
        if i in b:
            count += 1
    print(count)
str = input("Enter a string : ")
vowel_occurence(str)