import numpy as np

# Create a 1D array from 1 to 6.
flat_arr = np.arange(1, 7)  # [1, 2, 3, 4, 5, 6]

# Reshape it into a 2-row by 3-column matrix.
grid = flat_arr.reshape(3, 2)

print("Reshaped Matrix (2x3):\n", grid)

# Flatten the matrix back into a single 1D array.
print("Flattened back to 1D:", grid.flatten())
