def number():
    list=['imagination','parishmita',"maansi","tanvi",'shrusti',('devansh','manav','divyam',"akshat",'neel','shyam')]
    boys=0
    girls=0
    for i in list:
        if isinstance(i, tuple):
            boys +=len(i)
        else:
            girls += 1
    print("number of the girls: ",girls)
    print("number of the boys: ",boys)
number()