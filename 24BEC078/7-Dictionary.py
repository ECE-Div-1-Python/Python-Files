#1.	Write a program to create three dictionaries and concatenate them to create fourth dictionary.
def dictionary1():
    d1={1:10,2:20,3:30}
    d2={"a1":90,"a2":250}
    d3={"Name":"Kripa","Department":"ECE"}
    d4={**d1,**d2,**d3}
    print(d4)

dictionary1()
"""-----------------------------------------------------------------------------------------------------------------"""
#2.	Write a program to check whether a dictionary is empty or not.
def dictionary2():
    d1={1:20}
    if not d1:
        print("Empty dictionary")
    else:
        print("Not empty dictionary") 
    print(bool(d1))
    
dictionary2()

"""-----------------------------------------------------------------------------------------------------------------"""
#3.	Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary
def department_salary():
    employees = [
        (101, "E001", 50000), (102, "E002", 60000), (101, "E003", 45000),
        (103, "E004", 70000), (102, "E005", 80000), (103, "E006", 75000),
        (101, "E007", 55000), (102, "E008", 62000)
    ]

    salary_data = {}

    for dept, _, salary in employees:
        if dept not in salary_data:
            salary_data[dept] = {"min_salary": salary, "max_salary": salary}
        else:
            salary_data[dept]["min_salary"] = min(salary_data[dept]["min_salary"], salary)
            salary_data[dept]["max_salary"] = max(salary_data[dept]["max_salary"], salary)

    for dept, salary in salary_data.items():
        print(f"Department {dept}: Min Salary = {salary['min_salary']}, Max Salary = {salary['max_salary']}")

department_salary()

"""-----------------------------------------------------------------------------------------------------------------"""
#4.	Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string.
def dictionary4():
    s = input("Enter string: ")
    freq_dict = {}  

    for char in s:  
        if char in freq_dict:
            freq_dict[char] += 1 
        else:
            freq_dict[char] = 1 

    print("Character Frequency Dictionary:", freq_dict)

dictionary4()

"""-----------------------------------------------------------------------------------------------------------------"""
"""5.	Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased.
By using the values from these two dictionaries compute the total bill."""
def total_bill():
    prices = {
        "Rice": 50, 
        "Wheat": 40, 
        "Sugar": 30, 
        "Milk": 25, 
        "Eggs": 5
    }

    quantity = {
        "Rice": 2, 
        "Wheat": 3, 
        "Sugar": 1, 
        "Milk": 5, 
        "Eggs": 12
    }

    bill = 0

    for item in prices:
        if item in quantity:
            bill += prices[item] * quantity[item]

    print(f"Total Bill: ₹{bill}")

total_bill()