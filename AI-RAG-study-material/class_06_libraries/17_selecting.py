import pandas as pd

# Create a DataFrame with a custom row index.
df = pd.DataFrame({"Item": ["A", "B", "C"], "Qty": [10, 20, 30]}, index=["row1", "row2", "row3"])

# Select a single column as a Series.
print("Column Selection:\n", df["Item"])

# Select a row by its label using .loc.
print("\nLabel Selection (.loc):\n", df.loc["row2"])

# Select a row by its integer position using .iloc.
print("\nPosition Selection (.iloc):\n", df.iloc[0])
