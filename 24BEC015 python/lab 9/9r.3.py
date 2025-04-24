#Count No. of Vowel in String
def Count_vowel(s2,count,l1,idxl,idxs):
    if(idxl!=len(l1)):
        if(idxs!=len(s2)):
            if(l1[idxl]==s2[idxs]):
                return Count_vowel(s2,count+1,l1,idxl,idxs+1)
            else:
                return Count_vowel(s2,count,l1,idxl,idxs+1)
        else:
            return Count_vowel(s2,count,l1,idxl+1,idxs=0) 
    else:
        return count

    '''for i in l1:
        for j in s2:
            if(i==j):
                count += 1
    return count'''

s1 = input("Enter a string : ")
s2 = s1.upper()
count = 0
idxl = 0
idxs = 0
l1 = ['A','E','I','O','U']
print("No. of vowel in string : ",Count_vowel(s2,count,l1,idxl,idxs))