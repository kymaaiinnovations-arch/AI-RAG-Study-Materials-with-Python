"""
Definition: Demonstrate Figure and Axes using `subplots()`.
Why: Shows difference between the whole window and the plotting area.
Real-world Example: Multiple plots in one dashboard window.
Installation: `pip install matplotlib` if needed.

File: 02_figure_axes.py
"""

import matplotlib.pyplot as plt

# Create a figure and one axes (subplot)
figure, axis = plt.subplots()

# Plot some data on the axes
axis.plot([1, 2, 3], [2, 4, 6], marker='o')

# Add labels and title to the axes
axis.set_title('Figure and Axes Example')
axis.set_xlabel('X')
axis.set_ylabel('Y')

# Display the plot
plt.show()

# Expected Output: Single plot inside a window with markers.

# Practice Exercise: Create a second axes in the same figure using `plt.subplots(1,2)` and plot different data.
