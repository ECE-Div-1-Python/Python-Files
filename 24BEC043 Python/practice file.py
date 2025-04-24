'''f=open("C:\\Users\\lab\\Desktop\\vi.csv","w")
#roll number, Name , Hindi, Maths,Physics
f.write("roll_number,Name,Hindi,Maths,Physics,\n")
rlno=input("Enter your Roll.no[press enter to quit]:")
while rlno:
    nm=input("Enter your Name:")
    h,m,p=input("Enter marks of Hindi, Maths, Physics:").split(",")
    f.write(rlno+","+nm+","+h+","+m+","+p+"\n")
    rlno=input("Enter your Rollnumber[press enter to quit]")
    

f.close()
    
'''
import csv

with open("C:\\Users\\lab\\Desktop\\dh.csv","a",newline="")as f:
    writer=csv.writer(f)
    writer.writerow(["Name","Roll_number","CPII"])
    writer.writerow(["Saurabh","24bec980","98"])
f.close()

'''f.write("Vidhi,\n")
f.write("Adraja")
f.write("Adraja")
f.close()'''

