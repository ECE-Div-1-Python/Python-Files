def count_upper_lower(s):

    dict={"upper":0,"lower":0}
    for i in s:
        if i.isupper():

            dict["upper"]+=1
        else:

            dict["lower"]+=1
    return dict

str=input("enter the string:")
a=count_upper_lower(str)
print(a)








