# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Mean
print("The mean of the matrix is: {}".format(np.mean(matrix)))

# Variance
print("The variance of the matrix is: {}".format(np.var(matrix)))

# Standard Deviation
print("The standard deviation of the matrix is: {}".format(np.std(matrix)))

# Find the mean value in each column
print("The mean value in each columns is: {}".format(np.mean(matrix, axis=0)))
