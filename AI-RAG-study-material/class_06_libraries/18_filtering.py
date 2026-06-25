import pandas as pd

# Create a DataFrame with student names and marks.
df = pd.DataFrame({"Name": ["John", "Sara", "Tom"], "marks": [60, 85, 90]})

# Filter rows where the marks column is greater than 75.
filtered_df = df[df["marks"] > 75]
print(filtered_df)
