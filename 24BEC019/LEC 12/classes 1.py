class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        return f"({self.r}{self.i:+}i)"

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __sub__(self,other):
        return complex(self.r -other.r, self.i - other.i)
    def __mul__(self,other):
        return complex((self.r*other.r)-(self.i*other.i),(self.i*other.r) + (self.r*other.i))
    def __truediv__(self, other):
        denominator = other.r ** 2 + other.i ** 2
        real = (self.r * other.r + self.i * other.i) / denominator
        imag = (self.i * other.r - self.r * other.i) / denominator
        return complex(real, imag)

a = Complex(9, -5)
b = Complex(4, 3)

print(a+b)
print(a - b)
print(a * b)
print(a/b)


































