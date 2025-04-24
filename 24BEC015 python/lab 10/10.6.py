def q6():
    f_in1=open("6_in1.txt",'r')
    f_in2=open("6_in2.txt",'r')
    f_out=open("6_out.txt",'w')
    data1=f_in1.readlines()
    data2=f_in2.readlines()
    length=max(len(data1),len(data2))
    for i in range(length):
        if(i<len(data1)):
            f_out.write(data1[i])
        if(i<len(data2)):
            f_out.write(data2[i])
    print("Done")
    f_in1.close()
    f_in2.close()
    f_out.close()
q6()
