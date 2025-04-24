def convert_to_binary(no):
    if(no==0):
        return ""
    else:
        return convert_to_binary(no//2)+str(no%2==0)
no = int(input("Enter a number : "))
print(convert_to_binary(no))