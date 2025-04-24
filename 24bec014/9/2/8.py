def q8():
    def string_length(s:str)->int:
        if s == "":  
            return 0
        return 1 + string_length(s[1:])
    s=input("Enter any string:")
    print("Length of given string is",string_length(s))
q8()