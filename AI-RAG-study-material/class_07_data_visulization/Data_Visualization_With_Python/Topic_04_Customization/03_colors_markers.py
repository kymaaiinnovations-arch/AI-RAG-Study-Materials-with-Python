"""
Colors and markers lesson

Definition: Change colors and markers to improve readability.
Why: Different colors/markers help distinguish series.
File: 03_colors_markers.py
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x, y, color='red', marker='s', linestyle='--')
plt.title('Colors and Markers')

plt.show()

# Practice: Try different marker shapes and colors.
