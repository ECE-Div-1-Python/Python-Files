def tuple3():
 students = [(45, 'rohit', 37), (33, 'hardik', 32), (18, ' kohli', 37),(66,'surya',35)]
 roll_no = []
 name = []
 age = []
 for student in students:
    roll_no.append(student[0])  
    name.append(student[1])    
    age.append(student[2])    


 print("Roll Numbers:", roll_no)
 print("Names:", name)
 print("Ages:", age)

tuple3()
