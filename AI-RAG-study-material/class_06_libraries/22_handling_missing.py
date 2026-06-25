import pandas as pd
import numpy as np

# Create a DataFrame with one missing value.
df = pd.DataFrame({"Values": [10, np.nan, 30]})

# Replace missing values with 0.
print("Filled with 0:\n", df.fillna(0))

# Forward fill missing values using the last valid value.
print("\nForward Filled:\n", df.ffill())
