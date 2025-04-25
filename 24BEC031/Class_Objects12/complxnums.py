class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        den = other.real ** 2 + other.imag ** 2
        if den == 0:
            raise ValueError("Cannot divide by zero")
        real = (self.real * other.real + self.imag * other.imag) / den
        imag = (self.imag * other.real - self.real * other.imag) / den
        return Complex(real, imag)

if __name__ == "__main__":
    c2 = Complex(2, 3)
    c1 = Complex(4, 15)
    add_r = c1 + c2
    print(f"Addition: {c1} + {c2} = {add_r}")

    sub_r = c1 - c2
    print(f"Subtraction: {c1} - {c2} = {sub_r}")

    mul_r = c1 * c2
    print(f"Multiplication: {c1} * {c2} = {mul_r}")

    try:
        div_r = c1 / c2
        print(f"Division: {c1} / {c2} = {div_r}")
    except ValueError as e:
        print(e)
