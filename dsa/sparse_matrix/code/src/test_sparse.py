from sparse_matrix import SparseMatrix

file1 = "/dsa-sparse-matrix/dsa/sparse_matrix/sample_inputs/matrix1.txt"
file2 = "/dsa-sparse-matrix/dsa/sparse_matrix/sample_inputs/matrix2.txt"

matrix1 = SparseMatrix(file1)
matrix2 = SparseMatrix(file2)

print("Matrix 1:")
matrix1.display()

print("\nMatrix 2:")
matrix2.display()

result = matrix1.add(matrix2)

print("\nResult of Addition:")
result.display()
