# convert the number in the word of speling 
#take input as a number from the user 
number=int(input("enter the number in between 0 to 19 :"))
if number>19 or number<0:
    print("invalid number ,please enter thr new number ")
word = [  "zero","one","two","three","four","five","six","seven","eight","nine","ten"
        "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen"
        ,"nineteen"]
if number <=19 or number>=0:
    print("number to word is :",  word[number])
else :
    print( "number out of the range ")
print (f"the number {number } in thhe word is :" , word[number ])