'''
Create a dictionary with dept no, employee roll no. and salary. Find out deparment wise min 
and maxi salary.
'''
d = {'HR':[[101,10000],[103,12000],[105,14000]],'IT':[[102,12000],[104,14000],[106,15000]]}
l_HR = []
l_IT = []
for i,(k,v) in enumerate(d.items()):
    if(k=='HR'):
        for i in v:
            for j in i:
                l_HR.append(j)
    if(k=='IT'):
        for i in v:
            for j in j:
                l_IT.append(j)
print("Minimum salary in HR : ",min(l_HR))
print("Maximum salary in HR : ",min(l_HR))
print("Minimum salary in IT : ",min(l_IT))
print("Maximum salary in IT : ",min(l_IT))