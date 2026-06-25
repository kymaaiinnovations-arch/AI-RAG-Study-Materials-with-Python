"""
Scatter Plot lesson

Definition: Scatter plots show relationships between two variables.
Why: To see correlation or clustering.
Real-world Example: Hours studied vs marks obtained.
Installation: `pip install matplotlib`
File: 03_scatter_plot.py
"""

import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
marks = [45, 50, 60, 75, 90]

plt.scatter(hours, marks, c='purple')
plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")

plt.show()

# Expected Output: Points roughly trending upward.

# Practice: Color points by a third variable (e.g., attendance).
