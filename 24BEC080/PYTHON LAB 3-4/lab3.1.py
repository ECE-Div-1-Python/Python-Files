def c1():
  str = input("Enter the string: ")
  vowels = "aeiouAEIOU"
  count = 0
  for char in str:
   if char in vowels:
      count += 1

      
      print("The numbers of vowels in the string is : ",count) 


c1()
