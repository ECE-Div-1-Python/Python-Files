class matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return matrix([[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)])

    def __mul__(self, other):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return matrix(result)

    def transpose(self):
        return matrix([[self.data[j][i] for j in range(3)] for i in range(3)])

    def __str__(self):
        return "\n".join(str(row) for row in self.data)

m1 = matrix([[1,-6,3],[4,5,6],[7,-8,9]])
m2 = matrix([[9,-8,7],[6,-5,4],[3,-2,1]])
print("Matrix Add:\n", m1 + m2)
print("Matrix Mul:\n", m1 * m2)
print("Transpose:\n", m1.transpose())