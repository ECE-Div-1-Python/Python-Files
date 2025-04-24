lst = ['madam','Python',"malayalam",12321]
palindrome=filter(lambda x:str(x)==str(x)[::-1],lst)
print(list(palindrome))