1)

import csv(1)

with open("students.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Subject1", "Subject2", "Subject3"])
    writer.writerow([1, "Alice", 85, 90, 88])
    writer.writerow([2, "Bob", 78, 76, 80])
    writer.writerow([3, "Charlie", 92, 89, 94])


2)

import csv(2)

students_dict = {}
with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        roll_no = row["Roll No"]
        total = int(row["Subject1"]) + int(row["Subject2"]) + int(row["Subject3"])
        students_dict[roll_no] = {
            "Name": row["Name"],
            "Subject1": int(row["Subject1"]),
            "Subject2": int(row["Subject2"]),
            "Subject3": int(row["Subject3"]),
            "Total": total
        }

print(students_dict)


3)

name = input("Enter full name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD
"""

with open("contact.vcf", "w") as file:
    file.write(vcard)

print("vCard created successfully!")


4)

import os
import shutil

os.makedirs("new_folder", exist_ok=True)
shutil.copy("old_folder/sample.txt", "new_folder/sample.txt")  # Adjust paths as needed

5)

with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    for line in src:
        dest.write(line.upper())
6)

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as fout:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    max_len = max(len(lines1), len(lines2))
    
    for i in range(max_len):
        if i < len(lines1):
            fout.write(lines1[i])
        if i < len(lines2):
            fout.write(lines2[i])

7)

import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def __str__(self):
        return f"{self.empcode}, {self.empname}, {self.doj}, {self.salary}"

emp = Employee(101, "John Doe", "2020-01-15", 55000)

with open("employee.pkl", "wb") as file:
    pickle.dump(emp, file)

with open("employee.pkl", "rb") as file:
    loaded_emp = pickle.load(file)
    print(loaded_emp)

8)

with open("original.txt", "r") as infile, open("cleaned.txt", "w") as outfile:
    for line in infile:
        words = line.split()
        filtered = [word for word in words if word.lower() not in ("a", "the", "an")]
        outfile.write(" ".join(filtered) + "\n")

