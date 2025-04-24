def convertbytes():
    bytesvalue = int(input("Enter the number of bytes: "))
    kb = bytesvalue / 1024 
    mb = kb / 1024         
    gb = mb / 1024          
    
    print(f"{bytesvalue} bytes is equal to:")
    print(f"{kb:.2f} KB")
    print(f"{mb:.2f} MB")
    print(f"{gb:.2f} GB")


convertbytes()
