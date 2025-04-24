marks1 = int(input("Enter a mark1 : "))
marks2 = int(input("Enter a mark2 : "))
marks3 = int(input("Enter a mark3 : "))
print("sum = ",marks1+marks2+marks3)
print("average = ",(marks1+marks2+marks3)/3)
if(marks1<=39 or marks2<=39 or marks3<=39):
    print("Student is fail.")

if(marks1<=39 and marks1>=0):
    print("F")
elif(marks1<=44 and marks1>=40):
    print("P")
elif(marks1<=49 and marks1>=45):
    print("C")
elif(marks1<=54 and marks1>=50):
    print("B")
elif(marks1<=59 and marks1>=55):
    print("B+")
elif(marks1<=69 and marks1>=60):
    print("A")
elif(marks1<=79 and marks1>=70):
    print("A+")
elif(marks1<=100 and marks1>=80):
    print("O")

if(marks2<=39 and marks2>=0):
    print("F")
elif(marks2<=44 and marks2>=40):
    print("P")
elif(marks2<=49 and marks2>=45):
    print("C")
elif(marks2<=54 and marks2>=50):
    print("B")
elif(marks2<=59 and marks2>=55):
    print("B+")
elif(marks2<=69 and marks2>=60):
    print("A")
elif(marks2<=79 and marks2>=70):
    print("A+")
elif(marks2<=100 and marks2>=80):
    print("O")

if(marks3<=39 and marks3>=0):
    print("F")
elif(marks3<=44 and marks3>=40):
    print("P")
elif(marks3<=49 and marks3>=45):
    print("C")
elif(marks3<=54 and marks3>=50):
    print("B")
elif(marks3<=59 and marks3>=55):
    print("B+")
elif(marks3<=69 and marks3>=60):
    print("A")
elif(marks3<=79 and marks3>=70):
    print("A+")
elif(marks3<=100 and marks3>=80):
    print("O")