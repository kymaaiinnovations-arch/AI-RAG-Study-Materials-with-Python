import pandas as pd

# Create a DataFrame with one repeated row.
df = pd.DataFrame({"Item": ["Pen", "Pen", "Cup"]})

# Show which rows are duplicates.
print("Is Duplicated?:\n", df.duplicated())

# Remove duplicate rows and keep only the first occurrence.
print("\nCleaned of Duplicates:\n", df.drop_duplicates())
