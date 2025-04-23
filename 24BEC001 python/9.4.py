l1 = []
for i in range(0,5):
    n = int(input("Enter a marks : "))
    l1.append(n)
def sum_avg(list):
    sum = 0
    for i in list:
        sum = sum + i
    avg = sum/5
    print("sum : ", sum)
    print("average : ", avg)
print(sum_avg(l1))