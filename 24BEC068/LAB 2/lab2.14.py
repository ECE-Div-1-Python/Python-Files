def b14():
    
    s1 = int(input("Enter the math mark: "))
    s2 = int(input("Enter the chemistry mark: "))
    s3 = int(input("Enter the physics mark: "))

    
    if (s1 < 0) or (s1 > 100) or (s2 < 0) or (s2 > 100) or (s3 < 0) or (s3 > 100):
        print("Invalid marks! Please enter marks between 0 and 100.")
    else:
    
        if (s1 < 40) or (s2 < 40) or (s3 < 40):
            print("Fail")
        else:
            
            average = (s1 + s2 + s3) / 3

            
            if 40 <= average <= 44:
                print("P")
            elif 45 <= average <= 49:
                print("C")
            elif 50 <= average <= 54:
                print("B")
            elif 55 <= average <= 59:
                print("B+")
            elif 60 <= average <= 69:
                print("A")
            elif 70 <= average <= 79:
                print("A+")
            elif 80 <= average <= 100:
                print("O")


b14()

