import pandas as pd

# Create a DataFrame with clean status data.
df = pd.DataFrame({"Status": ["Clean", "Ready"], "Code": [200, 201]})

# Save the DataFrame to a CSV file without row index numbers.
df.to_csv("cleaned_output.csv", index=False)

# Save the DataFrame to a JSON file.
df.to_json("cleaned_output.json")

print("Files successfully exported.")
