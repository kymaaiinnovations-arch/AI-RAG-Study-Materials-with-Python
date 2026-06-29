import pandas as pd

# Create a DataFrame directly from a Python dictionary.
dict_data = {"City": ["New York", "Paris"], "Pop": [8.4, 2.1]}
df_dict = pd.DataFrame(dict_data)
print("From Dict:\n", df_dict)

# Example of how you would read from a CSV file instead.
# df_csv = pd.read_csv('data.csv')
