l1 = []
for i in range(0,5):
    name = input("Entre a name : ")
    l1.append(name)
s1 = set(l1)
while 1:
    print("1 == To modify name.")
    print("2 == To delete name.")
    print("3 == To Exit")
    c = int(input("Enter a choice : "))
    if(c==1):
        x = input("Enter a name to modify : ")
        y = input("Enter modify name : ")
        l2 = list(s1)
        no = 0
        for i in l2:
            if(x==i):
                l2[no] = y
            no += 1
        s2 = set(l2)
        print(s2)
    elif(c==3):
        break
    else:
        print("Invalid Enter.")