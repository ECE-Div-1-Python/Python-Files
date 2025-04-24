def q2():
    def binary(n:int):
        if n == 0:
            return
        binary(n // 2)
        print(n % 2, end='')

    num = int(input("Enter a positive integer: "))

    if num == 0:
        print("0")
    else:
        binary(num)

q2()