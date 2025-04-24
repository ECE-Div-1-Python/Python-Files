class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)
    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real, imaginary)

    def __str__(self):
        sign = '+' if self.imaginary >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imaginary)}i"


c1 = ComplexNumber(4, 5)    
c2 = ComplexNumber(2, -3)  

print("First Complex Number: ", c1)
print("Second Complex Number:", c2)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)
