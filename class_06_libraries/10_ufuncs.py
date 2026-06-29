import numpy as np

# Create numeric data for fast math operations.
data = np.array([10, 20, 30, 40])

# Use NumPy universal functions for summary statistics.
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Std Dev:", np.std(data))
print("Max/Min:", np.max(data), "/", np.min(data))
