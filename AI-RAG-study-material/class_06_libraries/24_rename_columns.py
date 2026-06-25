import pandas as pd

# Create a DataFrame with a column name that has extra spaces.
df = pd.DataFrame({" Old_Col ": [1, 2]})

# Strip spaces and convert the column name to lowercase.
df.columns = df.columns.str.strip().str.lower()

# Rename the cleaned column name to a more user-friendly name.
df = df.rename(columns={"old_col": "new_name"})

print(df)
