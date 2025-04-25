import json
from datetime import datetime

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = doj
        self.salary = salary

    def __repr__(self):
        return f"Employee(empcode={self.empcode}, empname='{self.empname}', date_of_joining='{self.date_of_joining}', salary={self.salary})"

    def to_dict(self):
        return {
            'empcode': self.empcode,
            'empname': self.empname,
            'date_of_joining': self.date_of_joining.strftime('%Y-%m-%d'),
            'salary': self.salary
        }

    @staticmethod
    def from_dict(data):
        date_of_joining = datetime.strptime(data['date_of_joining'], '%Y-%m-%d')  # Convert string back to date
        return Employee(
            empcode=data['empcode'],
            empname=data['empname'],
            doj=date_of_joining,
            salary=data['salary']
        )

def ser_emp(emp, filename):
    with open(filename, 'w') as file:
        json.dump(emp.to_dict(), file, indent=4)
    print(f"Employee object serialized and saved to '{filename}'.")

def des_emp(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return Employee.from_dict(data)


emp1 = Employee(
    empcode=101,
    empname="JIJI",
    doj=datetime(2020, 5, 15),  # Use datetime for Date of Joining
    salary=9999999999999999999999
)

filename = "employee.json"
ser_emp(emp1, filename)

emp2 = des_emp(filename)

print("Deserialized Employee Object:\n")
print(emp2)
