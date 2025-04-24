'''
a=3+6j          #in python it somehow consider "i" as an invalid decimal literal
b=4-3j          #and "j" as the complex one 
print(a,type(a))
print(b,type(b))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
'''
class xcomplex:
     def __init__(self,r=0,i=0):
          self.r=r
          self.i=i
     def __str__(self):
          return f'({self.r}{self.i:+}i)' #this ":+" will take the default as + when the number is non negative
     def __add__(self,other):
          return f'({self.r+ other.r}{self.i+other.i:+}i)'
     def __sub__(self,other):
          return f'({self.r- other.r}{self.i-other.i:+}i)'
     def __mul__(self,other):
          return f'({self.r*other.r}{self.i*other.i:+}i)'
     def __truediv__(self,other):
          return f'({self.r//other.r}{self.i//other.i:+}i)'
     def __truediv__(self,other):
          return f'({self.r/other.r}{self.i/other.i:+}i)'
          



     
c=xcomplex()
a=xcomplex(3,6)
b=xcomplex(4,-3)
print(c)
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)


