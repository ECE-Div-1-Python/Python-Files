class Matrix:
    def __init__(self, matrix):
        if len(matrix) == 3 and all(len(row) == 3 for row in matrix):
            self.matrix = matrix
        else:
            raise ValueError("Matrix must be 3x3.")

    def __repr__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if isinstance(other, Matrix):
            res = [[self.matrix[i][j] + other.matrix[i][j] for j in range(3)] for i in range(3)]
            return Matrix(res)
        else:
            raise ValueError("Both operands must be Matrix instances.")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            res = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(3)) for j in range(3)] for i in
                      range(3)]
            return Matrix(res)
        else:
            raise ValueError("Both operands must be Matrix instances.")

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)


if __name__ == "__main__":
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    print("Matrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    res_add = matrix1 + matrix2
    print("\nMatrix Addition (Matrix1 + Matrix2):")
    print(res_add)

    res_mul = matrix1 * matrix2
    print("\nMatrix Multiplication (Matrix1 * Matrix2):")
    print(res_mul)

    res_tpose = matrix1.transpose()
    print("\nTranspose of Matrix1:")
    print(res_tpose)
