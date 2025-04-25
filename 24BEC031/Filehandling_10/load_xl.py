import openpyxl

file = "files/students.xlsx"
wb = openpyxl.load_workbook(file)
sheet=wb.active
stu_data = {}

for row in sheet.iter_rows(min_row=2, values_only=True):
    RNo, name, m1, m2, m3 = row
    total = m1 + m2 + m3
    stu_data[RNo] = {
        "Name": name,
        "Marks": [m1, m2, m3],
        "Total": total
    }

print("Student Records:\n")
for RNo, details in stu_data.items():
    print(f"Roll No: {RNo}")
    print(f"Name   : {details['Name']}")
    print(f"Marks  : {details['Marks']}")
    print(f"Total  : {details['Total']}")
