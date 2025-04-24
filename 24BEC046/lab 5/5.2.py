import random
list = []
for i in range(0,20):
    list.append(random.randint(0,10))
print(list)

int = int(input("Enter a number between 0 to 10 to check occurence in list : "))
for i in range(0,len(list)):
    if(int==list[i]):
        print("index =", i)
else:
    print("Number not found.")
count = list.count(int)