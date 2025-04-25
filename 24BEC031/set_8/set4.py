#Defined a Set of names with initials 'A' and 'B'
s={"Albert Camus","Aurelius","Aphrodite","Birb","Bubble tart","Blimp"}

def set4():
    #defined two sets to segregate and sort the original set into
    s1 = set()
    s2 = set()
    #looped in s to traverse the set
    for i in s:
        #looped in each element of the set
        for j in i:
            #indexed the initial and checked if it was A
            if j[0]=="A":
                #added to s1 if the initial is A
                s1.add(i)
            #indexed the initial and checked if it was B
            elif j[0]=="B":
                #added to s1 if the initial is A
                s2.add(i)
    #printed both sorted sets
    print(s1)
    print(s2)
#called the earlier defined function
set4()