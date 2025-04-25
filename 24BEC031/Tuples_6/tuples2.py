def func(tuplis):
    rl=list()
    nl=list()
    al=list()

    for j in tuplis:
        rl.append(j[0])
        nl.append(j[1])
        al.append(j[2])

    print("Rollno:",rl)
    print("Name:",nl)
    print("Age:",al)



func([(0,'kafka',2),(1,'camus',5),(2,'zerotwo',50)])