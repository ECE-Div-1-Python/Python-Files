def fibonacci(n):
    list = [0, 1]
    while len(list) < n:
        list.append(list[-1] + list[-2])
    return list

n = int(input("enter the value of n: "))
print(fibonacci(n))