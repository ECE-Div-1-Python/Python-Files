employees=[{'dept no.':1,'emp_roll no.':101,"salary":60000},
            {'dept no.':1,'emp_roll no.':102,"salary":65000},
            {'dept no.':2,'emp_roll no.':201,"salary":70000},
            {'dept no.':2,'emp_roll no.':202,"salary":68000},
            {'dept no.':3,'emp_roll no.':301,"salary":45000},
            {'dept no.':3,'emp_roll no.':302,"salary":62000},
            ]

dept_s={}
for emp in employees:
    dept_no=emp['dept no.']
    salary=emp['salary']

    if dept_no not in dept_s:
        dept_s[dept_no]=[]

    dept_s[dept_no].append(salary)

dept_m={}
for dept,salaries in dept_s.items():
    dept_m[dept]={
        "min-salary":min(salaries),
        "max-salary":max(salaries)
    }
for dept,min_max in dept_m.items():
    print(f'department{dept}:')
    print(f"minimum salary: {min_max['min-salary']}")
    print(f"maximum salary: {min_max['max-salary']}")
