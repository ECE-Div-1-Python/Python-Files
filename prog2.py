import pandas as pd

# Load the Excel file (make sure the file is in the same directory)
df = pd.read_excel('students.xlsx', engine='openpyxl')

# Ensure subject columns are numeric and fill missing values with 0
df[['Subject1', 'Subject2', 'Subject3']] = df[['Subject1', 'Subject2', 'Subject3']].apply(pd.to_numeric, errors='coerce').fillna(0)

# Calculate total marks
df['Total'] = df['Subject1'] + df['Subject2'] + df['Subject3']

# Create a dictionary to store student data
students_dict = {}
for index, row in df.iterrows():
    roll_no = row['RollNo']
    if pd.isna(roll_no):
        continue  # Skip if RollNo is missing
    students_dict[roll_no] = {
        'Name': row['Name'],
        'Subject1': row['Subject1'],
        'Subject2': row['Subject2'],
        'Subject3': row['Subject3'],
        'Total': row['Total']
    }

# Print the student data
for roll_no, data in students_dict.items():
    print(f"Roll No: {roll_no}")
    for key, value in data.items():
        print(f"  {key}: {value}")
    print()
