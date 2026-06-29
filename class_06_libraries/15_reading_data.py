import pandas as pd
import io

# Simulate CSV file contents using a string.
csv_data = "ID,Name\n1,Alpha\n2,Beta"

# Read the CSV string into a DataFrame.
df = pd.read_csv(io.StringIO(csv_data))
print(df)
