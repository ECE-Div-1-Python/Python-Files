s=set()
print("Enter 5 unique names into a set\n")
for i in range(0, 5):
    s.add(input())
def set3():
    print("Enter the element to modify\n")
    m=(input())
    print("Enter the modification\n")
    m1=(input())
    for j in s:
        if j==m:
            s.remove(j)
            s.add(m1)
    s.pop()
    s.pop()
    print("The set is: ",s)

set3()