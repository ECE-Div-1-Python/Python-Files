class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        if self.imag >= 0:
            print(f"{self.real} + {self.imag}i")
        else:
            print(f"{self.real} - {-self.imag}i")

    def add(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return ComplexNumber(real_part, imag_part)

    def subtract(self, other):
        real_part = self.real - other.real
        imag_part = self.imag - other.imag
        return ComplexNumber(real_part, imag_part)

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def divide(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, -3)

print("First Complex Number:")
c1.display()

print("Second Complex Number:")
c2.display()

print("\nAddition:")
result = c1.add(c2)
result.display()

print("\nSubtraction:")
result = c1.subtract(c2)
result.display()

print("\nMultiplication:")
result = c1.multiply(c2)
result.display()

print("\nDivision:")
result = c1.divide(c2)
result.display()
