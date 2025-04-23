#q1
"""import csv
data = [
    ["Name", "Age", "City"],
    ["Alia", 25, "Bhopal"],
    ["Navya", 19, "New Delhi"],
    ["vidhi", 31, "Chennai"],
    ["Soumya", 40, "Bengaluru"]
]

filename = "people.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerows(data)

print(f"CSV file '{filename}' has been created successfully!")"""
#q1

"""f = open("C:\\Users\\lab\\Downloads\\people.csv","w")
f.write ("Alia,")
f.write ("Sharma")
f.write ("1234567789")

f.close()"""

#q2
"""f = open("C:\\Users\\lab\\Downloads\\people.csv","w")
f.write("roll no, name, maths,physics,chemistry")
rlno = input("enter your roll no. [press enter to quit]")
while rlno:
    nm = input("enter your name:")
    c,m,p = input("enter the marks of maths,physics, chemistry").split(" " )
    f.write(rlno + "," +nm+","+c+","+m+","+p+"\n")
    rlno = input("enter your roll no. [press enter to quit]")
f.close()"""
#q3
"""f = open("C:\\Users\\lab\\Downloads\\people.csv","a")
f.write("roll no, name, maths,physics,chemistry")
rlno = input("enter your roll no. [press enter to quit]")
while rlno:
    nm = input("enter your name:")
    c,m,p = input("enter the marks of maths,physics, chemistry").split(" " )
    f.write(rlno + "," +nm+","+c+","+m+","+p+"\n")
    rlno = input("enter your roll no. [press enter to quit]")
f.close()"""
#q4
"""import os    # Helps us work with folders
import shutil  # Helps us copy files

# Step 1: Set the path of the file you want to copy
source_file = "Users\sriva\Downloads\APPLICATIONS_OF_SECOND-ORDER_DIFFERENTIA (1).pdf"  # This is where the file is now

# Step 2: Set the name of the folder you want to create
new_folder = 'new'  # This is the new folder

# Step 3: Check if the new folder already exists
if not os.path.exists(new_folder):
    os.mkdir(new_folder)  # Create the folder if it doesn't exist
    print("New folder created:", new_folder)
else:
    print("Folder already exists:", new_folder)

# Step 4: Copy the file into the new folder
# We need to build the full path to where the file will go
destination_file = new_folder + "Users\sriva\Downloads\APPLICATIONS_OF_SECOND-ORDER_DIFFERENTIA (1).pdf"

try:
    shutil.copy(source_file, destination_file)
    print("File copied successfully!")
except FileNotFoundError:
    print("The file you're trying to copy does not exist.")
except Exception as error:
    print("Something went wrong:", error)"""
#q5
"""# Step 1: Open the source file for reading
try:
    with open('source.txt', 'r') as source_file:
        # Step 2: Read the contents of the file
        content = source_file.read()

        # Step 3: Convert all lowercase letters to uppercase
        content_upper = content.upper()

        # Step 4: Open the destination file for writing
        with open('destination.txt', 'w') as destination_file:
            destination_file.write(content_upper)

        print("File copied successfully with lowercase letters changed to uppercase.")

except FileNotFoundError:
    print("Error: 'source.txt' not found.")
except Exception as e:
    print("An error occurred:", e)"""
#q6
"""# Open both source files for reading
try:
    with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
        # Read all lines from both files
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Create a new file to write the merged lines
    with open('merged.txt', 'w') as output:
        # Get the length of the longer file
        max_len = max(len(lines1), len(lines2))

        # Loop through each line index
        for i in range(max_len):
            if i < len(lines1):
                output.write(lines1[i].rstrip() + '\n')
            if i < len(lines2):
                output.write(lines2[i].rstrip() + '\n')

    print("Files merged successfully into 'merged.txt'.")

except FileNotFoundError as e:
    print("Error: One of the input files was not found.")
    print(e)
except Exception as e:
    print("An error occurred:", e)"""
#q7
"""# Step 1: Create the Employee class
class Employee:
    def _init_(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary

    def display(self):
        print("Employee Code:", self.empcode)
        print("Employee Name:", self.empname)
        print("Date of Joining:", self.date_of_joining)
        print("Salary:", self.salary)

# Step 2: Create an employee object
emp = Employee(101, "Alice", "2022-03-15", 55000)

# Step 3: Save employee data to a text file (Serialization)
with open("employee.txt", "w") as file:
    file.write(str(emp.empcode) + "\n")
    file.write(emp.empname + "\n")
    file.write(emp.date_of_joining + "\n")
    file.write(str(emp.salary) + "\n")
    print("Employee data saved to 'employee.txt'.")

# Step 4: Read employee data from the text file (Deserialization)
with open("employee.txt", "r") as file:
    code = int(file.readline().strip())
    name = file.readline().strip()
    joining_date = file.readline().strip()
    salary = float(file.readline().strip())

# Step 5: Create a new Employee object from the read data
new_emp = Employee(code, name, joining_date, salary)

print("\nEmployee data read from file:")
new_emp.display()"""
#q8
"""# List of words to remove
remove_words = ['a', 'an', 'the']

# Step 1: Open the original file to read
with open('source.txt', 'r') as infile:
    content = infile.read()

# Step 2: Replace the words with blank spaces
words = content.split()  # Split text into a list of words
filtered_words = [word for word in words if word.lower() not in remove_words]  # Remove 'a', 'an', 'the'

# Step 3: Join the words back into a single string
cleaned_text = ' '.join(filtered_words)

# Step 4: Write the cleaned text to a new file
with open('destination.txt', 'w') as outfile:
    outfile.write(cleaned_text)

print("File processed successfully! Cleaned content saved in 'destination.txt'.")"""