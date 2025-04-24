def numberofgirlsandboys ():
    b=('kishan','rohit','surya','hardik','boult')
    s=[b,'geeta','sita','reeta','rani']
    countboys=0
    countgirls=0
    for i in s:
     if isinstance(i,tuple):
         for j in i:
          countboys=countboys+1
     else:
        countgirls=countgirls+1
    print(countboys)
    print(countgirls)

numberofgirlsandboys ()            
            
