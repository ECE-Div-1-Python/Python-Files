'''class Mycomplex_number:
    n1_r = 4
    n1_i = 4
    n2_r = 5
    n2_i = 5
obj1 = Mycomplex_number()
print(obj1.n1_r,"+ i",obj1.n1_i)
print(obj1.n2_r,"+ i",obj1.n2_i)
print("Addition : ",obj1.n1_r+obj1.n2_r,"+ i",obj1.n1_i+obj1.n2_i)
print("Subtraction : ",obj1.n1_r-obj1.n2_r,"+ i",obj1.n1_i-obj1.n2_i)'''

class Complex_Number:
    def __init__(self,r,i):
        self.r = r
        self.i = i
        print("In init")

    def print_cn(self):
        print(self.r,"+i",self.i)

    def __del__(self):
        print("Memory will free")

cn1 = Complex_Number(1,1)
print(cn1.print_cn())

cn2 = Complex_Number(2,2)
print(cn2.print_cn())