def calculateaverageandtotal():
    subject1 = float(input("Enter marks for subject 1: "))
    subject2 = float(input("Enter marks for subject 2: "))
    subject3 = float(input("Enter marks for subject 3: ")) 
    
    total = subject1 + subject2 + subject3
    average = total / 3
    
    print(f"Total Marks: {total:.2f}")
    print(f"Average Marks: {average:.2f}")


calculateaverageandtotal()
