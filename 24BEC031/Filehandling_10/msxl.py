import csv

data = [
    ["Name", "Department", "Salary"],  # Header row
    ["Luna", "catnip meownagement", '5 fis'],
    ["Jinx", "finance meownister", '7 bisket'],
    ["Bingus", "Tech expurrt", '2 pyramids']
]


with open("files/Meows.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully!")
