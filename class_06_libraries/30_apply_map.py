import pandas as pd

# Create a DataFrame with numeric scores and gender codes.
df = pd.DataFrame({"Scores": [10, 20, 30], "Gender": ["m", "f", "m"]})

# Use apply() with a lambda to double each score.
df["Double_Score"] = df["Scores"].apply(lambda x: x * 2)

# Use map() to replace gender codes with full labels.
df["Gender_Full"] = df["Gender"].map({"m": "Male", "f": "Female"})

print(df)
