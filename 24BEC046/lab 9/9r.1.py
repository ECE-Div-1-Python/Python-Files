'''def prime_factor(number,l2=[]):
    l1 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    for i in range(0,len(l1)):
        if(number%l1[i]==0):
            number = number/l1[i]
            l2.append(l1[i])
        if(i>=14 and number!=1):
            prime_factor(number)
    l2.sort()
    return l2'''
def prime_factor(number,l1,i=0):
    if (number==1):
        return ""
    if(number%l1[i]==0):
        return prime_factor(number//l1[i],l1,i=i+1) + str(l1[i])
    if(i>=14 and number!=1):
        return prime_factor(number,l1,i=0)
number = int(input("Enter a number : "))
l1 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(prime_factor(number,l1))