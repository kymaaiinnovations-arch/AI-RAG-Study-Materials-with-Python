import numpy as np

# Create a NumPy array for vectorized math.
arr = np.array([1, 2, 3, 4])
print("Original:", arr)

# Multiply each element by 10 without a Python loop.
print("Multiplied by 10:", arr * 10)

# Add the array to itself element-wise.
print("Added to self:", arr + arr)
print("Added to self:", arr + 5)
