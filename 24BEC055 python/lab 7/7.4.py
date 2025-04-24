s1 = input("Enter a string : ")
s2 = s1.upper()
l1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l2 = []
for i in l1:
    count = 0
    for j in s2:
        if(i==j):
            count += 1
    l2.append(count)
#print(l2)
for i in range(len(l1)):
    print(l1[i]," : ",l2[i])