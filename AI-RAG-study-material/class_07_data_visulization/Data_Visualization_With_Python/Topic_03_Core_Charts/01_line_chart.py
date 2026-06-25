"""
Line Chart lesson

Definition: Line charts show changes over time.
Why: To visualise trends across ordered data (e.g., months).
Real-world Example: Monthly sales over a year.
Installation: `pip install matplotlib`
File: 01_line_chart.py
"""

import matplotlib.pyplot as plt

# Months and sales data
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [120, 150, 180, 220]

# Draw line chart
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# Expected Output: A line connecting monthly sales points.

# Practice: Add more months and use a dashed line style.
