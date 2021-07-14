# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a function that adds 100 to something


def add_100(i):
    return i + 100


# Create vectorized function
vectorized_add_100 = np.vectorize(add_100)

# Apply function to all elements in matrix
print("The original matrix is:\n{}".format(matrix))
print("The vectorized matrix is:\n{}.".format(vectorized_add_100(matrix)))

# Broadcasting
print("Using broadcasting, the solution we get is:\n{}".format(matrix + 100))
