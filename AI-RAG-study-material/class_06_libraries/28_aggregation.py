import pandas as pd

# Create a DataFrame of department salaries.
df = pd.DataFrame({
    "Dept": ["HR", "IT", "IT", "HR"],
    "Salary": [50000, 70000, 80000, 52000]
})

# Calculate average salary for each department.
print("Mean Salary by Department:\n", df.groupby("Dept").mean())

# Count how many rows belong to each department.
print("\nTotal Count by Department:\n", df.groupby("Dept").count())
