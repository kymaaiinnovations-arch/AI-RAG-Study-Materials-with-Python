# Import the libraries used for numeric arrays and table data.
import numpy as np
import pandas as pd

# Create a NumPy array: all values share the same type.
num_array = np.array([1, 2, 3, 4])
print("NumPy Array:", num_array)

# Create a Pandas DataFrame from a dictionary of lists.
# Each column can hold a different type of data.
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
