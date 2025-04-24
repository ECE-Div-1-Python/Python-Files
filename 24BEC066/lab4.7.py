
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
n_fact = 1
for i in range(1, n + 1):
 n_fact *= i
r_fact = 1
for i in range(1, r + 1):
 r_fact *= i
n_r_fact = 1
for i in range(1, n - r + 1):
 n_r_fact *= i
nCr = n_fact // (r_fact * n_r_fact)
nPr = n_fact // n_r_fact
print("The nCr is",nCr)
print("The nPr is",nPr)


