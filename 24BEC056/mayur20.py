print("calculate the net salary ")
gross_salary=float(input("enter the gross salary of month :"))
allowances=gross_salary*(0.1)
print(allowances)
deduction=gross_salary*(0.03)
print(deduction)
net_salary=gross_salary+allowances-deduction
print(net_salary)
