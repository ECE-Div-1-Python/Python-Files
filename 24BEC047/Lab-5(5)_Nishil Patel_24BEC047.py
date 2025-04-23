# list contain string convert in upper case

list = ["A","b","C","d","E"]
listU = []
for i in list:
    y = ord(i)
    if(y<=123 and y>=97):
        y = y - 32
        listU.append(chr(y))
    else:
        listU.append(i)
print(listU)