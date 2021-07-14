# Load library
import numpy as np

# Create row vector
vector = np.array([1, 2, 3, 4, 5, 6])

# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Select third element of a vector
print("The third element of the vector is: ")
print(vector[2])

# Select second row, second column
print("The element at second row and second column is: ")
print(matrix[1, 1])

# Select all elements of a vector
print("All elements in vector are:")
print(vector[:])

# Select everything up to and including the third element
print("All elements up to and including third element: ")
print(vector[:3])

# Select everything after third element
print("All elements after the third element: ")
print(vector[3:])

# Select the last element
print("The last element in the vector is: ")
print(vector[-1])

# Select the first two rows and all columns of a matrix
print("The first 2 rows and all columns of the matrix are: ")
print(matrix[:2, :])

# Select all rows and the second column
print("All the rows and second column is: ")
print(matrix[:, 1:2])
