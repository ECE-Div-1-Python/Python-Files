import csv

# Data to write into the CSV file
data = [
    ["Roll No", "Name", "Subject1", "Subject2", "Subject3", "Total"],
    [1, "John", 80, 75, 90, 245],
    [2, "Alice", 85, 78, 88, 251],
    [3, "Bob", 70, 85, 92, 247]
]

# Creating a CSV file
with open('students.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully.")







import pandas as pd

# Reading the Excel file
df = pd.read_excel('students.xlsx')

# Convert the data into dictionary
data_dict = df.to_dict(orient='records')

# Calculate total for each student
for record in data_dict:
    record['Total'] = sum([record['Subject1'], record['Subject2'], record['Subject3']])

# Display the dictionary data
print(data_dict)








def create_vcard():
    # Accepting user input
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    # Creating a vCard file
    vcard_content = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:{address}
END:VCARD
"""

    # Writing the vCard to a file
    with open(f"{name}.vcf", "w") as vcard_file:
        vcard_file.write(vcard_content)

    print(f"vCard for {name} has been created successfully.")

create_vcard()






import os
import shutil

# Create a subdirectory
subdirectory_path = 'new_subdir'
os.makedirs(subdirectory_path, exist_ok=True)

# Define the source and destination files
source_file = 'source_file.txt'
destination_file = os.path.join(subdirectory_path, 'copied_file.txt')

# Copy the file to the new subdirectory
shutil.copy(source_file, destination_file)

print(f"File copied to {destination_file}.")






def copy_and_convert():
    with open('source_file.txt', 'r') as src, open('destination_file.txt', 'w') as dest:
        for line in src:
            dest.write(line.upper())

    print("Contents copied and converted to uppercase.")

copy_and_convert()
