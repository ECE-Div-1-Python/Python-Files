# 1. Concatenate three dictionaries to create a fourth dictionary
def concatenate_dictionaries():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict3 = {'e': 5, 'f': 6}

    concatenated_dict = {**dict1, **dict2, **dict3}
    print("Concatenated Dictionary:", concatenated_dict)

# 2. Check whether a dictionary is empty or not
def check_empty_dict():
    dictionary = {}
    if not dictionary:
        print("The dictionary is empty.")
    else:
        print("The dictionary is not empty.")

# 3. Find department-wise minimum and maximum salary
def department_salary_stats():
    employees = {
        101: {'dept': 'HR', 'salary': 50000},
        102: {'dept': 'IT', 'salary': 60000},
        103: {'dept': 'HR', 'salary': 55000},
        104: {'dept': 'IT', 'salary': 70000},
        105: {'dept': 'Finance', 'salary': 80000},
        106: {'dept': 'Finance', 'salary': 75000}
    }

    dept_salary = {}
    for emp, details in employees.items():
        dept = details['dept']
        salary = details['salary']
        if dept not in dept_salary:
            dept_salary[dept] = {'min': salary, 'max': salary}
        else:
            dept_salary[dept]['min'] = min(dept_salary[dept]['min'], salary)
            dept_salary[dept]['max'] = max(dept_salary[dept]['max'], salary)
    
    print("Department-wise Salary Stats (Min, Max):")
    for dept, salary_range in dept_salary.items():
        print(f"{dept}: Min Salary = {salary_range['min']}, Max Salary = {salary_range['max']}")

# 4. Create a dictionary containing frequency of each character in a string
def char_frequency():
    string = input("Enter a string: ")
    frequency_dict = {}

    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    print("Character frequency in the string:", frequency_dict)

# 5. Compute total bill using two dictionaries (grocery items, price, and quantity)
def calculate_bill():
    prices = {
        'apple': 3,
        'banana': 1,
        'cherry': 2,
        'date': 5
    }

    quantities = {
        'apple': 4,
        'banana': 6,
        'cherry': 3,
        'date': 2
    }

    total_bill = sum(prices[item] * quantities.get(item, 0) for item in prices)
    
    print("Total Bill:", total_bill)
