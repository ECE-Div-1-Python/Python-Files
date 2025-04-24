def a21():
    gross_salary = float(input("Enter gross salary: ")) 
    allowance = (0.10 * gross_salary)  
    deduction = (0.03 * gross_salary)  
    net_salary = gross_salary + allowance - deduction  
    print("Net Salary is:", net_salary)  

a21()
        
