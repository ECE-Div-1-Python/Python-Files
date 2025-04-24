def cv() :
 
    a = input("Enter a string: ")
    c = 0

    for ch in a :
        if ch in "AEIOUaeiou" :
            c += 1
    
    print("No. of vowels in string: ", c)

cv()