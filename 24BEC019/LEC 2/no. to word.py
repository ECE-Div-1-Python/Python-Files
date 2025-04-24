num=["zero","one","two","three","four","five","six","seven",'eigth','nine','ten','eleven','twelve',
     'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
a=int(input("enter the no.:  "))
if(0<=a<=19):
    print(a,"=",num[a])
else:
    print("out of the limit")
