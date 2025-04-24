no = 6

# code for prime no. checking

for i in range(2,no//2):
    if(no%i==0):
        print(no,"is not prime no.")
        break
else:
    print(no,"is prime no.")

# code for perfect square no. checking

for i in range(2,no//2):
    if(no/i==i):
        print(no,"is perfect square no.")
        break
else:
    print(no,"is not perect square no.")

# code for checking palindrome no.

temp = 0
a = no
while (a!=0):
    rem = a%10
    temp = 10*temp + rem
    a = a//10
if(temp==no):
    print(no,"is palindrome no.")
else:
    print(no,"is not palindrome no.")

# code for checking armstrong no.

temp = 0
b = no
while (b!=0):
    rem = b%10
    temp = temp + rem*rem*rem
    b = b//10
if(temp==no):
    print(no,"is armstrong no.")
else:
    print(no,"is not armstrong no.")

# code for checking automorphic no.

digit = 0
c = no
d = no
while (c!=0):
    rem = c%10
    digit = digit + 1
    c = c//10
e = (d*d)%(10**digit)
if(e==no):
    print(no,"is automorphic no.")
else:
    print(no,"is not auromorphic no.")