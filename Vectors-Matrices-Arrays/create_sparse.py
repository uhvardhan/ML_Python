# Load libraries
import numpy as np
from scipy import sparse

# Create a Matrix
matrix = np.array([[0, 0], [0, 1], [3, 0]])

matrix_large = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Create compressed sparse row (CSR) Matrix
matrix_sparse = sparse.csr_matrix(matrix)

matrix_large_sparse = sparse.csr_matrix(matrix_large)

# Print statements
print("This is sparse matrix:")
print(matrix_sparse)


print("This is larger sparse matrix:")
print(matrix_large_sparse)
