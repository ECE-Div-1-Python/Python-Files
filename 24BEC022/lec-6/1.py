def number():
    list=['imagination','parishmita',"foram","dhvani",'riddhi',('devansh','savar','divyam',"akshat",'kavish')]
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