str = input("Enter a String : ")
def count_letter(str):
    c_lower = 0
    for i in str:
        y = ord(i)
        if(y<=122 and y>=97):
            c_lower += 1
    c_upper = 0
    for i in str:
        y = ord(i)
        if(y<=90 and y>=65):
            c_upper += 1
    count1 = {"lower":c_lower,"upper":c_upper}
    return count1
print(count_letter(str))