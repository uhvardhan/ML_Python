# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# View the number of rows and columns
print("The number of rows in the matrix are {}.".format(matrix.shape[0]))
print("The number of columns in the matrix are {}.".format(matrix.shape[1]))

# View the number of elements (rows * columns)
print("The number of elements in the matrix are {}.".format(matrix.size))

# View the number of dimensions
print("The dimension of the matrix is {}.".format(matrix.ndim))
