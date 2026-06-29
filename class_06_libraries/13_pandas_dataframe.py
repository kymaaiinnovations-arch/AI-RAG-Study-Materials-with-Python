import pandas as pd

# Create dictionary data for a table.
data = {
    "Product": ["Laptop", "Mouse"],
    "Price": [1200, 25]
}

# Convert the dictionary to a DataFrame.
df = pd.DataFrame(data)
print(df)
