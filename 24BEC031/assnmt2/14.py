mk1=int(input("Enter marks in subject 1\n"))
mk2=int(input("Enter marks in subject 2\n"))
mk3=int(input("Enter marks in subject 3\n"))
grade='N/A'

tot=mk1+mk2+mk3
avg=(mk1+mk2+mk3)/3

if(mk1<=39 or mk2<=39 or mk3<=39):
    grade='F'
if(avg<40):
    grade='F'
elif(avg>=40 and avg<45):
    grade='P'
elif(avg>=45 and avg<50):
    grade='C'
elif(avg>=50 and avg<55):
    grade='B'
elif(avg>=55 and avg<60):
    grade='B+'
elif(avg>=60 and avg<70):
    grade='A'
elif(avg>=70 and avg<80):
    grade='A+'
elif(avg>80 and avg<=100):
    grade='O'
else:
    print("Please enter a valid value for marks")

print(grade)