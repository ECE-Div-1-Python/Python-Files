def ls1():                                              #Problem-1
    a= int(input("Enter no.a: "))
    b= int(input("Enter no.b: "))
    if(a>b):
        print("Greater:",a)
        print("Smaller:",b)

    elif(b>a):
        print("Greater:",a)
        print("SMaller:",b)    
    else:
        print("Both are equal") 

def ls2():                                              #Problem-2
    a= int(input("Enter no.a: "))
    b= int(input("Enter no.b: "))
    c= int(input("Enter no.c: "))
    if(a>b)and (a>c):
        print("Greatest:",a)
    elif(b>a)and (b>c):
        print("Greatest:",b)
    else:    
        print("Greatest:",c)
    if(a<b)and (a<c):
        print("Smallest:",a)
    elif(b<a)and (b<c):
        print("Smallest:",b)
    else:    
        print("Smallest:",c)

def ls3():                                              #Problem-3
        a= int(input("Enter no: "))
        if(a%2==0):
            print("Even")
        else:
            print("Odd")

def ls4():                                              #Problem-4
    a= int(input("Enter no: "))
    if(a%10==0):
        print("Divisible")
    else:
        print("Not divisible")

def ls5():                                              #Problem-5
    age= int(input("Enter age: "))
    if(age<18):
        print("Minor")
    else:
        print("Major")    

def ls6():                                              #Problem-6
    a= input("Enter number")
    print("Number of digits:",len(a))

def ls7():                                              #Problem-7
    year=int(input("Enter year"))
    if(year%4==0):
        print("Leap year")
    else:
        print("Not leap year")

def ls8():                                              #Problem-8
    a= int(input("Enter angle of triangle: "))
    b= int(input("Enter angle of triangle: "))
    c= int(input("Enter angle of triangle: "))
    if(a+b+c==180):
        print("Triangle is valid")
    else:
        print("Triangle is not valid")

def ls9():                                              #Problem-9
    a= int(input("Enter number"))
    if(a<0):
        print(a*(-1))
    else:
        print(a) 

def ls10():                                             #Problem-10
    l= int(input("Enter length"))
    b= int(input("Enter breath"))
    area=l*b
    p= 2*(l+b)
    if(area>p):
        print("Area is greater")

    elif(p>area):
        print("Perimeter is greater")
    else:
        print("Both are equal") 

def ls11():                                             #Problem-11
    x1=int(input("Enter x1:"))
    y1=int(input("Enter y1:"))
    x2=int(input("Enter x2:"))
    y2=int(input("Enter y2:"))
    x3=int(input("Enter x3:"))
    y3=int(input("Enter y3:"))
    if((y3-y2)/(x3-x2)==(y2-y1)/(x2-x1)):
        print("Points lie on line")
    else:
        print("Points do not lie on line")

def ls12():                                             #Problem-12
    r= 2
    Cx= 2
    Cy= 2
    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    if((x-Cx)**2+(y-Cy)**2>r**2):
        print("Point lies outside circle")
    elif((x-Cx)**2+(y-Cy)**2<r**2):
        print("Point lies inside circle")
    else:
        print("Point lies on circle")

def ls13():                                             #Problem-13
    x=int(input("Enter number from 1-19\n"))
    if x==0:
        print("Zero")
    elif x==1:
        print("One")
    elif x==2:
        print("Two")
    elif x==3:
        print("Three")
    elif x==4:
        print("Four")
    elif x==5:
        print("Five")
    elif x==6:
        print("Six")
    elif x==7:
        print("Seven")
    elif x==8:
        print("Eight")
    elif x==9:
        print("Nine")
    elif x==10:
        print("Ten")
    elif x==11:
        print("Eleven")
    elif x==12:
        print("Twelve")
    elif x==13:
        print("Thirteen")
    elif x==14:
        print("Fourteen")
    elif x==15:
        print("Fifteen") 
    elif x==16:
        print("Sixteen")
    elif x==17:
        print("Seventeen")
    elif x==18:
        print("Eighteen")
    elif x==19:
        print("Nineteen")

def ls14():                                             #Problem-14
    phy=int(input("Enter physics marks "))
    chem=int(input("Enter chemistry marks "))    
    math=int(input("Enter mathematics marks "))
    grad=""   
    total= phy+chem+math
    avg= total/3
    if(phy<=39) or (chem<=39) or (math<=39):
        print("FAIL")  
    else:
        print("PASS")
    def grade(marks):
        if(marks>80):
            grad="O"
        elif(70<marks<79):
            grad="A+"
        elif(60<marks<69):
            grad="A"
        elif(55<marks<59):
            grad="B+"
        elif(50<marks<54):
            grad="B"
        elif(45<marks<49):
            grad="C"
        elif(40<marks<44):
            grad="P"
        else:
            grad="F"
        return grad        
    print("Physics grade:",grade(phy))
    print("Chemistry grade:",grade(chem))
    print("Mathematics grade:",grade(math))
