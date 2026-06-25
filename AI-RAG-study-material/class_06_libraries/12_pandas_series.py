import pandas as pd

# Define values and labels for a Series.
scores = [85, 90, 78]
indices = ["Math", "Science", "History"]

# Create a Pandas Series with a custom index.
series = pd.Series(data=scores, index=indices)
print(series)
