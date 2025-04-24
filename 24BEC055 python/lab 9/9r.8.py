#find lenght of string using recursion
def len_str(s,length,idx):
    if(s[idx:]):
        length += 1
        return len_str(s,length,idx+1)
    else:
        return length

    '''for i in s:
        length += 1
    return length'''

s = input("Enter a string : ")
length = 0
idx = 0
print("length of string : ",len_str(s,length,idx))