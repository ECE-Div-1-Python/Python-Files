class Matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Only 3x3 matrices are supported.")
        self.data = data

    def __add__(self, other):
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)

    def __mul__(self, other):
        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)

    def transpose(self):
        result = [
            [self.data[j][i] for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)

    def display(self):
        for row in self.data:
            print(row)
        print()
A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = Matrix([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix A:")
A.display()

print("Matrix B:")
B.display()

C = A + B
print("A + B:")
C.display()

D = A * B
print("A * B:")
D.display()

print("Transpose of A:")
A_T = A.transpose()
A_T.display()

print("Transpose of B:")
B_T = B.transpose()
B_T.display()
