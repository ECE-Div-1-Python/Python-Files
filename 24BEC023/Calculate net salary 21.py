def calculatenetsalary():
    grosssalary = float(input("Enter the gross salary: "))
    allowance = 0.10 * grosssalary
    deduction = 0.03 * grosssalary
    
   
    netsalary = grosssalary + allowance - deduction

    print(f"Gross Salary: {grosssalary:.2f}")
    print(f"Allowance (10%): {allowance:.2f}")
    print(f"Deduction (3%): {deduction:.2f}")
    print(f"Net Salary: {netsalary:.2f}")


calculatenetsalary()
