
l = [("berry", 100), ("apple", 90), ("mango", 120), ("kiwi", 80)]


n = len(l)
for i in range(n):
    for j in range(0, n-i-1):
        if l[j][1] < l[j+1][1]:
            l[j], l[j+1] = l[j+1], l[j]

print(l)