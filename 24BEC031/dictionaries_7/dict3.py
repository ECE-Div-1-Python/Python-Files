from collections import defaultdict

# Sample data: list of (dept_no, emp_roll_no, salary)
employees = [
    (101, 1, 50000),
    (102, 2, 60000),
    (101, 3, 70000),
    (103, 4, 55000),
    (102, 5, 65000),
    (103, 6, 75000),
    (101, 7, 48000),
    (102, 8, 72000)
]

# Dictionary to store department-wise salaries
dept_salaries = defaultdict(list)

# Populate dictionary
for dept_no, emp_roll_no, salary in employees:
    dept_salaries[dept_no].append(salary)

# Compute min and max salary for each department
dept_salary_stats = {
    dept_no: {"min_salary": min(salaries), "max_salary": max(salaries)}
    for dept_no, salaries in dept_salaries.items()
}

# Output results
for dept, stats in dept_salary_stats.items():
    print(f"Department {dept}: Min Salary = {stats['min_salary']}, Max Salary = {stats['max_salary']}")
