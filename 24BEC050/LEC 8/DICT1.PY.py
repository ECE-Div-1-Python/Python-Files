def dict():
    D1={"S1":"PHYSICS","S2":"CHEMISTRY"}
    D2={"S3":"MATHS","S4":"ENGLISH"}
    D3={"S5":"IKS"}
    D4={**D1,**D2,**D3}
    print(D4)
dict()

