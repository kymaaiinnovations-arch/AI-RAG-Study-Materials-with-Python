import pandas as pd
import numpy as np

# Create a DataFrame with missing values in columns A and B.
df = pd.DataFrame({"A": [1, np.nan, 3], "B": [np.nan, np.nan, 6]})

# Count how many missing values appear in each column.
print("Missing Value Table Counts:")
print(df.isnull().sum())
