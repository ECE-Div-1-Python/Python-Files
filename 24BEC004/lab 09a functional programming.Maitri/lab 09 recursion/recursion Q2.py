def binary(n):
    global bin
    bin=''
    if n>1:
        binary(n//2)
    bin+=str(n%2)
    return bin
print(binary(17))