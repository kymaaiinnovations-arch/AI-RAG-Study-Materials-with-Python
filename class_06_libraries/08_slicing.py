import numpy as np

# Create a 1D NumPy array.
arr = np.array([10, 20, 30, 40, 50])

# Create a 2D NumPy matrix.
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Take a slice from index 1 up to, but not including, index 4.
print("1D Slicing (elements 1 to 3):", arr[1:4])

# Access the element in row 1, column 2 of the matrix.
print("Specific element from matrix [row 1, col 2]:", matrix[1, 2])
