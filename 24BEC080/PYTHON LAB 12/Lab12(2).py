class Matrix:
    def __init__(self, m):
        self.m = m

    def show(self):
        for r in self.m:
            print(r)

    def add(self, other):
        return Matrix([[self.m[i][j] + other.m[i][j] for j in range(3)] for i in range(3)])

    def multiply(self, other):
        return Matrix([[sum(self.m[i][k] * other.m[k][j] for k in range(3)) for j in range(3)] for i in range(3)])

    def transpose(self):
        return Matrix([[self.m[j][i] for j in range(3)] for i in range(3)])

m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[9,8,7],[6,5,4],[3,2,1]])

print("Matrix 1:"); m1.show()
print("\nMatrix 2:"); m2.show()

print("\nAddition:"); m1.add(m2).show()
print("\nMultiplication:"); m1.multiply(m2).show()
print("\nTranspose of Matrix 1:"); m1.transpose().show()
print("\nTranspose of Matrix 2:"); m2.transpose().show()
