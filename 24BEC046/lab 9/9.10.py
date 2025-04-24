def frequency(str):
    str1 = str.upper()
    print(str1)
    l1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    l2 = []
    for i in l1:
        count = 0
        for j in str1:
            if(i==j):
                count += 1
        l2.append(count)
    return (l1,l2)
str = input("Enter a string : ")
l1,l2 = frequency(str)
for i in range(0,26):
    print("The no. of ", l1[i],"is : ", l2[i])