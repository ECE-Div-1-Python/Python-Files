list = ['a','b','c']
l2 = []
for i in list:
    y = ord(i)
    if(y<=122 and y>=97):
        y = y - 32
    l2.append(chr(y))
s1 = {i for i in l2}
print(s1)