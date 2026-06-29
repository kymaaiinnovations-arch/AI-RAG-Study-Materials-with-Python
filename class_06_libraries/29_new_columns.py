import pandas as pd

# Create a DataFrame with price and quantity values.
df = pd.DataFrame({"Price": [100, 200], "Qty": [2, 3]})

# Add a new column by multiplying existing columns element-wise.
df["Total_Cost"] = df["Price"] * df["Qty"]
print(df)
