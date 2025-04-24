def ispalindrome(n):
    if(isinstance(n,int)==True):
        n = str(n)
    str1 = ""
    l = len(n)
    for i in range(l):
        str1 = str1 + n[l-1-i]
    return True if n==str1 else False
l1=['madam','Python',"malayam",12321]
p = filter(ispalindrome,l1)
print(list(p))