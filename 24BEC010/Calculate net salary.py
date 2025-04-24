#Calculate net salary
#where net salary = gross salary + allowance – deduction.
#Allowances are 10% while deductions are 3% of gross salary

s=float(input('enter gross salary: '))
a=0.1*s
d=0.03*s
print('net salary: ',s+a-d)