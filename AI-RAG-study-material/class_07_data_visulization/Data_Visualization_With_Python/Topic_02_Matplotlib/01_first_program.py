"""
Definition: A tiny matplotlib program that draws a line chart.
Why: To introduce plotting and `plt.show()`.
Real-world Example: Plot monthly sales to see the trend.
Installation: `pip install matplotlib` (if needed)

File: 01_first_program.py
"""

import matplotlib.pyplot as plt

# Data for x-axis (months)
x = [1, 2, 3, 4]
# Data for y-axis (sales)
y = [5, 10, 15, 20]

# Draw a line chart: x vs y
plt.plot(x, y)

# Add title and labels
plt.title("Simple Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")

# Display the chart window
plt.show()

# Expected Output: A window with a simple upward line.

# Practice Exercise: Change the data to show a dip in month 3.
