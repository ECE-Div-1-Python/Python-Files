def binary_equivalent(n):
    if n == 0:
        return ''
    return binary_equivalent(n // 2) + str(n % 2)
print(binary_equivalent(int(input("enter the number: "))))


