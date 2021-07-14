# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Return maximum element
print("The maximum element in the array is: {}".format(np.max(matrix)))

# Return the minimum element
print("The minimum element in the array is: {}".format(np.min(matrix)))

# Find maximum element in each column
print("The maximum element in each column is: {}".format(np.max(matrix, axis=0)))

# Find maximum element in each row
print("The maximum element in each row is: {}".format(np.max(matrix, axis=1)))
