import pandas as pd

# Create a DataFrame with a custom index order.
df = pd.DataFrame({"Age": [45, 22, 31]}, index=["b", "c", "a"])

# Sort rows by the Age column values.
print("Sort by Values (Age):\n", df.sort_values(by="Age"))

# Sort rows by the DataFrame index labels.
print("\nSort by Index:\n", df.sort_index())
