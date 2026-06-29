import pandas as pd

# Create a DataFrame with names that need cleaning.
df = pd.DataFrame({"Names": ["  alice ", "bob##", "CHARLIE"]})

# Remove extra spaces, delete '#' characters, and convert names to uppercase.
df["Names"] = df["Names"].str.strip().str.replace("#", "", regex=False).str.upper()
print(df)
