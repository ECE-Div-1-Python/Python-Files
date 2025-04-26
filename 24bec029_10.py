print("Name: Rutva Mehta")
print("Rollno.: 24BEE122")

# Define file names
input_file = "input.txt"
output_file = "cleaned_text.txt"

# Open the input file and read lines
with open(input_file, "r") as file:
    lines = file.readlines()

# List of words to remove
remove_words = ["a", "an", "the"]

# Process each line
with open(output_file, "w") as file:
    for line in lines:
        words = line.split()  # Split line into words
        new_words = [word for word in words if word.lower() not in remove_words]  # Remove unwanted words
        file.write(" ".join(new_words) + "\n")  # Write cleaned line

print(f"File '{output_file}' created successfully with words removed.")


import os

source_file = "source_folder/example.txt"
destination_dir = "destination_folder/new_subdir"
destination_file = os.path.join(destination_dir, "example.txt")

os.makedirs(destination_dir, exist_ok=True)

with open(source_file, "rb") as src:
    content = src.read()

with open(destination_file, "wb") as dst:
    dst.write(content)

print(f"Copied '{source_file}' to '{destination_file}' successfully.")



import csv

# Data to write
students = [
    ["Roll No", "Name", "Subject1", "Subject2", "Subject3"],
    [101, "Alice", 85, 90, 80],
    [102, "Bob", 75, 85, 95],
    [103, "Charlie", 90, 92, 88]
]

# Writing to CSV
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully.")
f=open('students.csv','w')






name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""

with open("contact.vcf", "w") as file:
    file.write(vcard_content)

print("vCard created successfully.")



source_file = "input.txt"
destination_file = "output.txt"

with open(source_file, "r") as src, open(destination_file, "w") as dest:
    for line in src:
        dest.write(line.upper())

print("File copied with content converted to uppercase into another.")





def merge_files_alternatively(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
     
        len1, len2 = len(lines1), len(lines2)
        
       
        for i in range(max(len1, len2)):
            if i < len1:
                out.write(lines1[i])
            if i < len2:
                out.write(lines2[i])

merge_files_alternatively('file1.txt', 'file2.txt', 'merged_output.txt')




import csv

# Data to write
students = [
    ["Roll No", "Name", "Subject1", "Subject2", "Subject3"],
    [101, "Alice", 85, 90, 80],
    [102, "Bob", 75, 85, 95],
    [103, "Charlie", 90, 92, 88]
]

# Writing to CSV
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully.")































