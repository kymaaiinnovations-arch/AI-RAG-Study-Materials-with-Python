import pandas as pd

# Create a DataFrame of department salaries.
df = pd.DataFrame({
    "Dept": ["HR", "IT", "IT", "HR"],
    "Salary": [50000, 70000, 80000, 52000]
})

# Group rows by the Dept column.
grouped = df.groupby("Dept")
print(grouped)  # This prints the groupby object, not the grouped data itself.
