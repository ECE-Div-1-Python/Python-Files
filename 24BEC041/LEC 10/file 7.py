import json
employee = {
    "empcode": 108,
    "empname": "Divyam Patel",
    "Date_of_Joining": "2024-06-10",
    "Salary": 100000
}
with open('files/file 7.txt', 'w+') as f:
   json.dump(employee, f)
   f.seek(0)
   a=json.load(f)
   print(a)