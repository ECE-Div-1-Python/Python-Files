f=open("files/file5_1.txt","r")
for line in f.readlines():
    s=line.strip().upper()

d=open("files/file5_2.txt","w")
d.write(s)
d.close()
f.close()
print("your data tyransfer successfully!")