''' take tthe three subject marks from the user and take  the average of the marks 
and decide the whether  he/she passed or fail and give grade acording to the  marks
 given by the user'''

# take the subject marks 
subject1=float(input("enter the first subject marks :"))
subject2=float(input("enter the second subject marks :"))
subject3=float(input("enter the third subject marks :"))
# take the average of the  subject 
average= (subject1+subject2+subject3)/3
print("average of the three subjects is : ",average)
if subject1 <=39:
    print ("sorry, you are fail in this subject ")
else:
    print ("you passed the the subject1 ")
if subject2<=39:
    print ("sorry, you are fail in this subject ")
else:
    print ("you passed the the subject2 ")
if subject3<=39:
    print ("sorry, you are fail in this subject ")
else:
    print ("you passed the the subject3 ")

    # give the grade of the subject  
if 0<=subject1<=39:
    print(" your subject1 grade is 'F'")
if 40<=subject1<=44:
    print(" your subject1 grade is 'P'")
if 45<=subject1<=49:
    print(" your subject1 grade is 'C'")
if 50<=subject1<=54:
    print(" your subject1 grade is 'B'")
if 55<=subject1<=59:
    print(" your subject1 grade is 'B+'")
if 60<=subject1<=69:
    print(" your subject1 grade is 'A'")
if 70<=subject1<=79:
    print(" your subject1 grade is 'A+'")
if 80<=subject1<=100:
    print(" your subject1 grade is 'O'")


if 0<=subject2<=39:
    print(" your subject2 grade is 'F'")
if 40<=subject2<=44:
    print(" your subject2 grade is 'P'")
if 45<=subject2<=49:
    print(" your subject2 grade is 'C'")
if 50<=subject2<=54:
    print(" your subject2 grade is 'B'")
if 55<=subject2<=59:
    print(" your subject2 grade is 'B+'")
if 60<=subject2<=69:
    print(" your subject2 grade is 'A'")
if 70<=subject2<=79:
    print(" your subject2 grade is 'A+'")
if 80<=subject2<=100:
    print(" your subject2 grade is 'O'")


if 0<=subject3<=39:
    print(" your subject33 grade is 'F'")
if 40<=subject3<=44:
    print(" your subject3 grade is 'P'")
if 45<=subject3<=49:
    print(" your subject3 grade is 'C'")
if 50<=subject3<=54:
    print(" your subject3 grade is 'B'")
if 55<=subject3<=59:
    print(" your subject3 grade is 'B+'")
if 60<=subject3<=69:
    print(" your subject3 grade is 'A'")
if 70<=subject3<=79:
    print(" your subject3 grade is 'A+'")
if 80<=subject3<=100:
    print(" your subject3 grade is 'O'")
