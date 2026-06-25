import pandas as pd

# Create a DataFrame where numbers and dates are stored as text.
df = pd.DataFrame({"Price": ["10", "20"], "Date": ["2026-01-01", "2026-01-02"]})

# Convert the Price column from strings to integers.
df["Price"] = df["Price"].astype(int)

# Convert the Date column from text to datetime objects.
df["Date"] = pd.to_datetime(df["Date"])

# Print the data types after conversion.
print(df.dtypes)
