
import pickle

class Employee:
    def _init_(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def display(self):
        print(f"Emp Code: {self.empcode}, Name: {self.empname}, DOJ: {self.doj}, Salary: {self.salary}")


emp = Employee(101, "Alice", "2022-05-10", 50000)

# Serialization
with open("employee.dat", "wb") as file:
    pickle.dump(emp, file)

# Deserialization
with open("employee.dat", "rb") as file:
    loaded_emp = pickle.load(file)

loaded_emp.display()
