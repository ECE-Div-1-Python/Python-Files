#1.	Write a program to create a csv file that we can directly open in MS-Excel.
import csv
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['RollNo', 'Name', 'Python', 'Maths', 'Physics'])
    writer.writerow([1, 'Alice', 85, 90, 88])
    writer.writerow([2, 'Bob', 78, 82, 80])
    writer.writerow([3, 'Charlie', 92, 87, 91])
print("CSV file 'students.csv' created.")
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#2.	Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monitor.
import csv
students = {}
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rollno = row['RollNo']
        name = row['Name']
        marks = [int(row['Python']), int(row['Maths']), int(row['Physics'])]
        total = sum(marks)
        students[rollno] = {'Name': name, 'Marks': marks, 'Total': total}
""" Display the dictionary"""
for roll, data in students.items():
    print(f"Roll No: {roll}, Name: {data['Name']}, Marks: {data['Marks']}, Total: {data['Total']}")
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#3.	Accept contact details from the user and create a vcard that we can directly store in our mobile.
name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD
"""
with open("contact.vcf", "w") as file:
    file.write(vcard)
print("vCard 'contact.vcf' created.")
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#4.	Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory.
import os
import shutil

source_dir = "source_folder"
target_dir = "target_folder"
file_to_copy = "example.txt"

os.makedirs(target_dir, exist_ok=True)
shutil.copy(os.path.join(source_dir, file_to_copy), target_dir)
print(f"File copied from {source_dir} to {target_dir}")
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#5.	Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters.
with open('input.txt', 'r') as source, open('output.txt', 'w') as target:
    for line in source:
        target.write(line.upper())

print("File copied to 'output.txt' with all lowercase letters converted to uppercase.")
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#6.	Write a program that merges lines alternatively from two files and writes the results to new file. If one file has less number of lines than the other,  the remaining lines from the larger file should be simply copied into the target file.
with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2, open('merged.txt', 'w') as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    
    max_len = max(len(lines1), len(lines2))
    
    for i in range(max_len):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])

print("Files merged alternately into 'merged.txt'")
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#7.	If an Employee object contains following details:
"""empcode, empname, Date of Joining, Salary
Write a program to serialize and deserialize this data."""
import pickle

class Employee:
    def __init__(self, code, name, doj, salary):
        self.code = code
        self.name = name
        self.doj = doj
        self.salary = salary

    def __str__(self):
        return f"Code: {self.code}, Name: {self.name}, DOJ: {self.doj}, Salary: {self.salary}"
# Serialization
emp = Employee(101, 'John Doe', '2020-01-01', 50000)
with open('employee.pkl', 'wb') as file:
    pickle.dump(emp, file)
# Deserialization
with open('employee.pkl', 'rb') as file:
    loaded_emp = pickle.load(file)

print("Deserialized Employee:", loaded_emp)
"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#8.	Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank space
remove_words = {'a', 'an', 'the'}

with open('original.txt', 'r') as file:
    text = file.read()

words = text.split()
cleaned_text = ' '.join(['' if word.lower() in remove_words else word for word in words])

with open('cleaned.txt', 'w') as file:
    file.write(cleaned_text)

print("Words 'a', 'an', 'the' removed in 'cleaned.txt'")
