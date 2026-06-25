import pandas as pd

# Create a sample DataFrame of scores.
df = pd.DataFrame({"Score": [45, 88, 92, 71, 60]})

# Show the first two rows of the DataFrame.
print("--- Head ---")
print(df.head(2))

# Show summary statistics for numeric columns.
print("\n--- Summary Stats ---")
print(df.describe())
