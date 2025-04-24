
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def divide(x,y):
    return x/y if y!=0 else "Cannot divide by zero"

num1=float(input("Enter first number :"))
num2=float(input("Enter second number :"))


def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choose= input("Enter your choice (1/2/3/4):")

    if choose == '1':
        print("Result:",{add(num1,num2)})
    elif choose =='2': 
        print("Result:",{sub(num1,num2)})
    elif choose =='3':
        print("Result:",{mult(num1,num2)})
    elif choose =='4':
        print("Result:",{divide(num1,num2)})
    else:
        print("Invalid inputs")

calculator()



def cal_sum(numbers):
    return sum(numbers)
def cal_average(numbers):
    return sum(numbers)/len(numbers)

numbers =[]

for i in range(0,5):
     num=float(input(f"Enter number {i+1}:"))
     numbers.append(num)

total= cal_sum(numbers)
average= cal_average(numbers)

print("Sum of numbers:",total)
print("Average of numbers:", average)




def factorial(a):
    for i in range (a):
        if (i !=0):
            a=a*i
        return (a)
def input_():
    a=int(input("Enter a number:"))
    b=factorial(a)

    print("The factorial of the number is:",b)
input_()





















