"""
Grid lesson

Definition: Add grid lines to help read values.
Why: Makes it easier to estimate values from the chart.
File: 04_grid.py
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x, y)
plt.grid(True)
plt.title('Grid Example')

plt.show()

# Practice: Make grid dashed by passing `linestyle='--'`.
