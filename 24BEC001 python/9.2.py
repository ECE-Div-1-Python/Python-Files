digit = int(input("Enter a number between 4 to 7 : "))
def value(n):
    total = 0
    sum = 0
    for i in range(1,digit+1):
        total = total*10+n
        sum = sum + total
    return sum
print(value(digit))