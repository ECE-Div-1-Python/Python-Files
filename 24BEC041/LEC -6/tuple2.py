def l():
    a=("24bcl007",18,18,17,18,'24bec082','24bec050','24bec031','neel','PARISHMITA','shyam','manav')
    name=[]
    age=[]
    roll=[]
    for i in range(0,len(a)):
        if isinstance(a[i],int):
            age.append(a[i])
        elif isinstance(a[i],str):
            if a[i].isalpha():
                name.append(a[i])
            else:
                roll.append(a[i])
    print("Name: ",name)
    print("Age: ",age)
    print("Roll: ",roll)
l()
