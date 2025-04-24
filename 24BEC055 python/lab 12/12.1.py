class xcomplex:
    def __init__(self, r=0, i=0):
        self.r = r
        self.i = i
    def __str__(self):
        return f'({self.r}{self.i:+}"i")'
    
    def __add__(self, other):
        ans=xcomplex()
        ans.r=self.r+other.r
        ans.i=self.i +other.i
        return ans
       
    def __sub__(self, other):
        ans=xcomplex()
        ans.r=self.r-other.r
        ans.i=self.i -other.i
        return ans
    def __mul__(self, other):
        ans=xcomplex()
        ans.r=self.r * other.r - self.i * other.i
        ans.i=self.r * other.i + self.i * other.r
        return ans
        
    def __truediv__(self, other):
        ans=xcomplex()
        ans.r=(self.r * other.r + self.i * other.i) /(other.r * other.r + other.i * other.i)
        ans.i= (self.i * other.r - self.r* other.i) /(other.r * other.r + other.i * other.i)
        return ans


a=xcomplex(9,-4)
b=xcomplex(2,11)
c=xcomplex()
print(a,b,c)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
        
