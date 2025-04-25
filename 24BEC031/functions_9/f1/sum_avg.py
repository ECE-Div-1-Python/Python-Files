def sum_avg(ls):
    sum=0
    for i in ls:
        sum+=i
    avg=sum/len(ls)
    return (f"Sum : {sum} \nAverage : {avg}")
print("Enter 5 numbers to calculate their sum and avg")
l=[]
for i in range(0,5):
    l.append(int(input()))
print(sum_avg(l))