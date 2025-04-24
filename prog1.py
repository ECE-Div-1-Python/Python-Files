
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



















