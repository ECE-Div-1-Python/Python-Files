text=input("Text :")
count =0
for character in text :
    if (character in "AEIOUaeiou"):
        count+=1

print("count :",count)
