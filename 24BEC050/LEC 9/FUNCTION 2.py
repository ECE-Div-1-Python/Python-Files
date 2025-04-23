def compute(n):
    s=str(n)
    sum=int(s)+int(s*2)+int(s*3)+int(s*4)
    return sum
for i in range(4,8):
    print(compute(i))

print(compute(int(input("enter the number: "))))







